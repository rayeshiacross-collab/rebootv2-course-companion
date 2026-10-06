# Persist records and verify a new load returns the same data.
import json
from pathlib import Path
def save_records(path, records):
    Path(path).write_text(json.dumps(records, indent=2), encoding='utf-8')
def load_records(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(data, list) or any(not isinstance(r, dict) or not isinstance(r.get('name'), str) or not r['name'].strip() for r in data):
        raise ValueError('Expected a list of named records')
    return data
if __name__ == '__main__':
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / 'characters.json'
        records = [{'name': 'Nova'}]
        save_records(path, records)
        print(load_records(path) == records)
