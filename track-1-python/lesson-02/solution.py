# Decomposition: each step has one action and an observable outcome.
STEPS = ['Show welcome', 'Get name', 'Search records', 'Handle missing match', 'Display card', 'Repeat or quit']
def pseudocode(steps):
    if not steps or any(not isinstance(s, str) or not s.strip() for s in steps):
        raise ValueError('Supply nonblank steps')
    return '\n'.join(f'# {i}. {step}' for i, step in enumerate(steps, 1))
if __name__ == '__main__':
    print(pseudocode(STEPS))
