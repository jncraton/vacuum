houses = [
"""
*********
*.......*
*.......*
*.......*
*.......*
*********
""",
]

def parse_house(house: str):
    """Converts string reprentation to 2d list
    
    >>> parse_house("***\\n*.*\\n*.*\\n***")
    [['*', '*', '*'], ['*', '.', '*'], ['*', '.', '*'], ['*', '*', '*']]
    """

    rows = [list(r) for r in house.strip().split('\n')]

    return rows

def ordered_agent(actions):
    """Handle one agent turn

    Returns exactly one action from list of valid actions
    """
    
    return actions[0]

def is_dirty(house: list):
    """Returns True if their is dirt in the house

    >>> is_dirty([['*', '*', '*'], ['*', '.', '*'], ['*', '*', '*']])
    True
 
    >>> is_dirty([['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']])
    False
    """

    for row in house:
        for cell in row:
            if cell == '.':
                return True

    return False

if __name__ == '__main__':
    house = parse_house(houses[0])

    for i in range(100):
        if is_dirty(house):
            print(f'Turn {i}')
            for row in house:
                print(''.join(row))
