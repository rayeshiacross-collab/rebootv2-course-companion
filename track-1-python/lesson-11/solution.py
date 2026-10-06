# Route commands separately from the interactive loop.
def route(choice, names):
    choice = choice.strip().casefold()
    if choice == '1':
        return ', '.join(names)
    if choice == 'q':
        return 'Goodbye'
    return 'Choose 1 or q'
if __name__ == '__main__':
    while True:
        result = route(input('1=list; q=quit: '), ['Nova', 'Orion'])
        print(result)
        if result == 'Goodbye': break
