# Expected user/file failures return a recovery message.
import json
from pathlib import Path
def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        return 'Create the data file first'
    except json.JSONDecodeError:
        return 'Repair the JSON syntax'
def positive_count(text):
    try:
        value = int(text)
    except ValueError:
        return 'Enter a whole number'
    return value if value > 0 else 'Enter a positive number'
if __name__ == '__main__':
    for value in ['3', 'hello', '0']:
        print(positive_count(value))
