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

def parse_house(house):
    """Converts string reprentation to 2d list
    
    >>> parse_house("***\\n*.*\\n*.*\\n***")
    [['*', '*', '*'], ['*', '.', '*'], ['*', '.', '*'], ['*', '*', '*']]
    """

    rows = [list(r) for r in house.split('\n')]

    return rows

if __name__ == '__main__':
    print(houses[0])
