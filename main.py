import time
from dataclasses import dataclass

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

def agent(actions):
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

@dataclass
class Direction:
    """
    >>> Direction('n')
    Direction(name='n')

    >>> d = Direction('n')
    >>> d.turn_cw(90)
    >>> d
    Direction(name='e')

    >>> d = Direction('n')
    >>> d.move((0,0))
    (0, -1)
    """
    name: str
    
    def turn_cw(self, angle):
        directions = 'nesw'

        direction = directions.index(self.name)
        direction = (direction + int(angle/90)) % 4

        self.name = directions[direction]

    def move(self, pos, distance=1):
        directions = {
            'n': ( 0,-1),
            'e': ( 1, 0),
            's': ( 0, 1),
            'w': (-1, 0),
        }

        return (
            pos[0] + distance * directions[self.name][0],
            pos[1] + distance * directions[self.name][1],
        )

    def __str__(self):
        return self.name    

if __name__ == '__main__':
    house = parse_house(houses[0])

    pos = (1, 1)
    facing = Direction('n')
    
    house[pos[1]][pos[0]] = 'O'

    for i in range(10):
        print(f'Turn {i}')
        for row in house:
            print(''.join(row))
        time.sleep(.1)

        actions = ['forward', 'left', 'right', 'backward']

        

        if not is_dirty(house):
            break
