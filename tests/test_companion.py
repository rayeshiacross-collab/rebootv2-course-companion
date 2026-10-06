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
    def run_lesson(self, number, supplied=None):
        source = ROOT / f"track-1-python/lesson-{number:02d}"
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for path in source.glob("*.py"):
                shutil.copyfile(path, folder/path.name)
            result = subprocess.run([sys.executable, "solution.py"], cwd=folder,
                input=(source/"input.txt").read_text() if supplied is None else supplied,
                text=True, capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            return result.stdout
    def test_all_solutions(self):
        for number in range(1,13):
            with self.subTest(lesson=number):
                expected=(ROOT/f"track-1-python/lesson-{number:02d}/expected.txt").read_text().strip()
                self.assertIn(expected, self.run_lesson(number))
    def test_condition_boundaries(self):
        for score, expected in [(90,"Excellent"),(70,"Passed"),(69,"Keep practicing")]:
            with self.subTest(score=score):self.assertIn(expected,self.run_lesson(4,f"{score}\n"))
    def test_bad_number(self):self.assertIn("valid whole number",self.run_lesson(10,"hello\n"))
    def test_zero(self):self.assertIn("cannot be zero",self.run_lesson(10,"0\n"))

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
