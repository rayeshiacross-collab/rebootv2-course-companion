"""Offline CSV-to-JSON record normalizer. Standard library only."""
import argparse
import csv
import json
import re
from pathlib import Path

def normalize_record(name, email):
    if not isinstance(name, str) or not isinstance(email, str):
        raise ValueError("name and email must be strings")
    name, email = name.strip(), email.strip().lower()
    if not name or not email:
        raise ValueError("name and email must not be blank")
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        raise ValueError("email does not match the basic exercise format")
    return {"name": name, "email": email}

def clean_rows(rows):
    records, rejected, seen = [], [], set()
    duplicates = 0
    for number, row in enumerate(rows, start=2):
        try:
            record = normalize_record(row.get("name"), row.get("email"))
        except (ValueError, AttributeError) as error:
            rejected.append({"row": number, "reason": str(error)})
            continue
        if record["email"] in seen:
            duplicates += 1
            continue
        seen.add(record["email"])
        records.append(record)
    return {"records": records, "rejected": rejected, "duplicates": duplicates}

def process_file(source, destination, overwrite=False):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError("input and output must be different files")
    with source.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {"name", "email"}.issubset(reader.fieldnames):
            raise ValueError("CSV must include name and email columns")
        result = clean_rows(reader)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w" if overwrite else "x", encoding="utf-8") as stream:
        stream.write(payload)
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        result = process_file(args.input, args.output, args.overwrite)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"Cannot complete the practice run: {error}\n")
    print(f"accepted={len(result['records'])}, rejected={len(result['rejected'])}, duplicates={result['duplicates']}")

if __name__ == "__main__":
    main()
