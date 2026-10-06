import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
app = load("capstone", "track-2-capstone/src/app.py")
sim = load("simulator", "track-3-automation/simulator.py")

class PythonExamples(unittest.TestCase):
    def lesson(self, n):
        return load(f"lesson{n}", f"track-1-python/lesson-{n:02}/solution.py")
    def test_all_examples_execute(self):
        for n in range(1,13):
            with self.subTest(lesson=n), tempfile.TemporaryDirectory() as tmp:
                source=ROOT/f"track-1-python/lesson-{n:02}"
                result=subprocess.run([sys.executable,str(source/'solution.py')],input=(source/'input.txt').read_text(),cwd=tmp,text=True,capture_output=True,timeout=10)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertTrue(result.stdout or result.stderr)
    def test_scope_rejects_blank_and_overscope(self):
        m=self.lesson(1);good=dict(user='Reader',problem='Search',input='Name',output='Card',features=['Search'])
        self.assertEqual(m.validate_brief(good),'Scope ready')
        for override in [dict(user=''),dict(features=[]),dict(features=['a']*4),dict(features=[''])]:
            with self.subTest(override=override),self.assertRaises(ValueError):m.validate_brief(dict(good,**override))
    def test_decomposition(self):
        m=self.lesson(2);self.assertEqual(len(m.pseudocode(m.STEPS).splitlines()),6)
        with self.assertRaises(ValueError):m.pseudocode([''])
    def test_greeting_validation(self):
        m=self.lesson(3);self.assertIn('Taylor',m.greet(' Taylor ','Nova'))
        with self.assertRaises(ValueError):m.greet(' ','Nova')
    def test_function_returns_record(self):
        m=self.lesson(4);records=[dict(name='Nova')]
        self.assertEqual(m.find_character(' NOVA ',records),records[0]);self.assertIsNone(m.find_character('',records))
    def test_branch_paths(self):
        m=self.lesson(5);names=['Nova','Nora']
        for q,expected in [('nova','Found: Nova'),('no','Suggestions: Nova, Nora'),('','Enter a name'),('zzz','Not found')]:
            self.assertEqual(m.search_characters(q,names),expected)
    def test_loop_search(self):
        m=self.lesson(6);self.assertEqual(m.search(' NOVA ',m.RECORDS),'Nova');self.assertEqual(m.search('',m.RECORDS),'Not found')
    def test_dictionary_duplicates(self):
        m=self.lesson(7)
        with self.assertRaises(ValueError):m.build_index([dict(name='Nova'),dict(name=' NOVA ')])
        with self.assertRaises(ValueError):m.build_index([dict(name='')])
    def test_json_roundtrip_and_shape(self):
        m=self.lesson(8)
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'data.json';records=[dict(name='Nova')];m.save_records(p,records);self.assertEqual(m.load_records(p),records)
            p.write_text('{}')
            with self.assertRaises(ValueError):m.load_records(p)
    def test_error_recovery(self):
        m=self.lesson(9);self.assertEqual(m.positive_count('3'),3);self.assertEqual(m.positive_count('0'),'Enter a positive number');self.assertEqual(m.positive_count('bad'),'Enter a whole number')
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'missing';self.assertEqual(m.read_json(p),'Create the data file first');p.write_text('{');self.assertEqual(m.read_json(p),'Repair the JSON syntax')
    def test_debugging_regressions(self):
        m=self.lesson(10);words=['Nova','Nora','Orion']
        for q,want in [('',[]),('NOVA',['Nova']),(' nova ',['Nova']),('missing',[]),('no',['Nova','Nora'])]:self.assertEqual(m.find_word(q,words),want)
    def test_menu_routes(self):
        m=self.lesson(11)
        for q,want in [('1','Nova'),('x','Choose 1 or q'),(' Q ','Goodbye')]:self.assertEqual(m.route(q,['Nova']),want)
    def test_lesson_twelve_search(self):
        m=self.lesson(12);self.assertEqual(m.find_name(' NOVA ',['Nova']),'Nova');self.assertIsNone(m.find_name('', ['Nova']))

class AutomationReferences(unittest.TestCase):
    def test_all_topic_packs_complete(self):
        for n in range(18,42):
            with self.subTest(lesson=n):
                p=ROOT/f'track-3-automation/lesson-{n:02}'
                b=json.loads((p/'blueprint.json').read_text());self.assertEqual(b['lesson'],n)
                self.assertTrue(b['required_fields']);self.assertEqual(set(b['required_fields']),set(b['field_mapping']))
                self.assertEqual(len(json.loads((p/'test-data.json').read_text())['cases']),4)
                self.assertTrue((p/'prompt.txt').read_text().strip());self.assertTrue((p/'system-instructions.txt').read_text().strip())

class Capstone(unittest.TestCase):
    def test_normalizes_without_recasing_name(self):
        self.assertEqual(app.normalize_record(" van Gogh "," USER@Example.com "),{"name":"van Gogh","email":"user@example.com"})
    def test_rejects_bad_fields(self):
        for name,email in [("","a@example.com"),(None,"a@example.com"),("A","bad"),("A","a @example.com"),("A",12)]:
            with self.subTest(email=email),self.assertRaises(ValueError):app.normalize_record(name,email)
    def test_deduplicates_and_rejects(self):
        result=app.clean_rows([{"name":"A","email":"a@example.com"},{"name":"B","email":" A@EXAMPLE.COM "},{"name":"","email":"c@example.com"}])
        self.assertEqual(len(result["records"]),1);self.assertEqual(result["duplicates"],1);self.assertEqual(len(result["rejected"]),1)
    def test_file_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/"result.json"
            result=app.process_file(ROOT/"track-2-capstone/fixtures/leads.csv",out)
            self.assertEqual(len(result["records"]),2)
            self.assertEqual(json.loads(out.read_text()),result)
            with self.assertRaises(FileExistsError):app.process_file(ROOT/"track-2-capstone/fixtures/leads.csv",out)
    def test_bad_headers_do_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);(p/"bad.csv").write_text("wrong\nx\n")
            with self.assertRaises(ValueError):app.process_file(p/"bad.csv",p/"out.json")
            self.assertFalse((p/"out.json").exists())
    def test_input_cannot_be_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"data.csv";p.write_text("name,email\nA,a@example.com\n")
            with self.assertRaises(ValueError):app.process_file(p,p,True)
            self.assertTrue(p.read_text().startswith("name,email"))

class Automation(unittest.TestCase):
    def setUp(self):
        self.event={"event_id":"test-1","name":"Morgan","email":"morgan@example.com","message":"product demo"}
        self.draft=sim.make_draft(self.event);self.sent=set();self.logs=[]
    def test_approved_and_duplicate(self):
        approval=sim.digest(self.draft)
        self.assertEqual(sim.execute(self.draft,approval,self.sent,self.logs),"simulated_sent")
        self.assertEqual(sim.execute(self.draft,approval,self.sent,self.logs),"duplicate_suppressed")
        self.assertEqual(len(self.sent),1)
    def test_pending_approval(self):
        self.assertEqual(sim.execute(self.draft,None,self.sent,self.logs),"approval_required");self.assertFalse(self.sent)
    def test_changed_draft(self):
        approval=sim.digest(self.draft);self.draft["body"]="Changed"
        self.assertEqual(sim.execute(self.draft,approval,self.sent,self.logs),"approval_required")
    def test_ambiguity(self):
        self.draft=sim.make_draft(dict(self.event,message="demo and charge"))
        self.assertEqual(sim.execute(self.draft,sim.digest(self.draft),self.sent,self.logs),"needs_review")
    def test_invalid_category(self):
        self.draft["decision"]={"status":"ok","category":"surprise"}
        self.assertEqual(sim.execute(self.draft,sim.digest(self.draft),self.sent,self.logs),"invalid_decision")
    def test_wrong_category_type(self):
        self.draft["decision"]={"status":"ok","category":["sales"]}
        self.assertEqual(sim.execute(self.draft,sim.digest(self.draft),self.sent,self.logs),"invalid_decision")
    def test_missing_input(self):
        for key in self.event:
            with self.subTest(key=key),self.assertRaises(ValueError):sim.make_draft(dict(self.event,**{key:""}))
    def test_failed_service_can_retry(self):
        approval=sim.digest(self.draft)
        self.assertEqual(sim.execute(self.draft,approval,self.sent,self.logs,False),"service_failed")
        self.assertFalse(self.sent)
        self.assertEqual(sim.execute(self.draft,approval,self.sent,self.logs),"simulated_sent")
    def test_logs_exclude_recipient_and_body(self):
        sim.execute(self.draft,sim.digest(self.draft),self.sent,self.logs)
        encoded=json.dumps(self.logs)
        self.assertNotIn(self.event["email"],encoded);self.assertNotIn(self.draft["body"],encoded)

if __name__ == "__main__":unittest.main()
