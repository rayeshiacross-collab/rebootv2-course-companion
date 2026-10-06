# Build a normalized index and reject duplicate names explicitly.
def build_index(records):
    index = {}
    for record in records:
        key = record['name'].strip().casefold()
        if not key or key in index:
            raise ValueError('Blank or duplicate character name')
        index[key] = record
    return index
if __name__ == '__main__':
    index = build_index([{'name': 'Nova', 'role': 'Explorer'}])
    print(index.get('nova'))
    print(index.get('missing', 'Not found'))
