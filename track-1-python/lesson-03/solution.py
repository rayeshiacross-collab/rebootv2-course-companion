# input returns text; keep the greeting deterministic for testing.
def greet(name, character):
    name, character = name.strip(), character.strip()
    if not name or not character:
        raise ValueError('Name and character are required')
    return f'Hello {name}! Your favorite character is {character}.'
if __name__ == '__main__':
    try:
        print(greet(input('Name: '), input('Character: ')))
    except ValueError as error:
        print(error)
