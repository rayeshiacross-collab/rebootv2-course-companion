# Guard blank input before exact and partial matching.
def search_characters(query, names):
    key = query.strip().casefold()
    if not key:
        return 'Enter a name'
    exact = [n for n in names if n.casefold() == key]
    if exact:
        return 'Found: ' + exact[0]
    partial = [n for n in names if key in n.casefold()]
    if partial:
        return 'Suggestions: ' + ', '.join(partial)
    return 'Not found'
if __name__ == '__main__':
    for query in ['nova', 'no', '', 'zzz']:
        print(search_characters(query, ['Nova', 'Nora']))
