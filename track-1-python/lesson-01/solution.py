# Represent a small project scope as data; validate before coding.
def validate_brief(brief):
    required = ('user', 'problem', 'input', 'output')
    if any(not isinstance(brief.get(k), str) or not brief[k].strip() for k in required):
        raise ValueError('Every brief needs user, problem, input and output')
    features = brief.get('features')
    if not isinstance(features, list) or not 1 <= len(features) <= 3:
        raise ValueError('Choose one to three must-have features')
    if any(not isinstance(x, str) or not x.strip() for x in features):
        raise ValueError('Features must be nonblank text')
    return 'Scope ready'
if __name__ == '__main__':
    print(validate_brief(dict(user='New reader', problem='Find a character', input='Name', output='Character card', features=['Search by name'])))
