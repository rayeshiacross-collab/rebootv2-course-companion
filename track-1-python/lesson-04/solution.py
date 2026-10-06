# A small pure function returns a value without reading input or printing.
def clean_input(value):
    return value.strip().casefold()
def find_character(name, records):
    key = clean_input(name)
    return next((r for r in records if key and clean_input(r['name']) == key), None)
if __name__ == '__main__':
    print(find_character('  nova ', [{'name': 'Nova', 'role': 'Explorer'}]))
