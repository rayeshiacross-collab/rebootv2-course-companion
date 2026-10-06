# Iterate over records and use q to exit the repeated search.
RECORDS = [{'name': 'Nova'}, {'name': 'Orion'}]
def search(query, records):
    key = query.strip().casefold()
    for record in records:
        if key and record['name'].casefold() == key:
            return record['name']
    return 'Not found'
if __name__ == '__main__':
    while True:
        query = input('Name (q to quit): ')
        if query.strip().casefold() == 'q':
            print('Goodbye'); break
        print(search(query, RECORDS))
