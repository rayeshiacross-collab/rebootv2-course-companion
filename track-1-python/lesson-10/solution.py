# Regression cases cover blanks, case, whitespace, missing and partial names.
def find_word(query, words):
    key = query.strip().casefold()
    if not key:
        return []
    return [word for word in words if key in word.casefold()]
if __name__ == '__main__':
    words = ['Nova', 'Nora', 'Orion']
    for query in ['', 'NOVA', ' nova ', 'missing', 'no']:
        print(find_word(query, words))
