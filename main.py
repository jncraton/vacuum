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

class Board:
    def __init__(self, definition):
        """Converts string reprentation to 2d list
        
        >>> Board("***\\n*.*\\n*.*\\n***")
        [['*', '*', '*'], ['*', '.', '*'], ['*', '.', '*'], ['*', '*', '*']]
        """

        self.rows = [list(r) for r in definition.strip().split('\n')]

    def get(self, pos):
        return self.rows[pos[1]][pos[0]]

    def set(self, pos, value):
        self.rows[pos[1]][pos[0]] = value

    def contains(self, char):
        """Returns True if their is dirt in the house

        >>> h = Board("***\\n*.*\\n*.*\\n***")
        >>> h.contains('.')
        True
     
        >>> h = Board("***\\n* *\\n* *\\n***")
        >>> h.contains('.')
        False
        """

        for row in self.rows:
            for cell in row:
                if cell == char:
                    return True

        return False



    def __repr__(self):
        return str(self.rows)

def agent(actions):
    """Handle one agent turn

    Returns exactly one action from list of valid actions
    """
    
    return actions[0]

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
        """
        >>> d = Direction('n')
        >>> d.turn_cw(-90)
        >>> d
        Direction(name='w')
        """
        directions = 'nesw'

        direction = directions.index(self.name)
        direction = (direction + int(angle/90)) % 4

        self.name = directions[direction]

    def move(self, pos, dist=1):
        """
        >>> d = Direction('w')
        >>> d.move((3,3), 4)
        (-1, 3)
        
        >>> d = Direction('s')
        >>> d.move((5,5), -2)
        (5, 3)

        >>> d = Direction('n')
        >>> d.move((5,5), 2)
        (5, 3)
        """

        directions = {
            'n': ( 0,-1),
            'e': ( 1, 0),
            's': ( 0, 1),
            'w': (-1, 0),
        }

        return (
            pos[0] + dist * directions[self.name][0],
            pos[1] + dist * directions[self.name][1],
        )

    def __str__(self):
        return self.name


if __name__ == '__main__':
    house = Board(houses[0])

    pos = (1, 1)
    facing = Direction('s')

    house.set(pos, facing.name)
    
    for i in range(100):
        print(f'Turn {i}')
        for row in house.rows:
            print(''.join(row))
        time.sleep(.2)

        actions = ['left', 'right']

        if house.get(facing.move(pos)) != '*':
            actions.insert(0, 'forward')

        action = agent(actions)

        assert(action in actions)

        house.set(pos, ' ')

        if action == 'left':
            facing.turn_cw(90)
        elif action == 'right':
            facing.turn_ccw(-90)
        elif action == 'forward':
            pos = facing.move(pos)

        house.set(pos, facing.name)

        if not house.contains('.'):
            break
