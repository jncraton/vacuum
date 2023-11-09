import random
import time
from dataclasses import dataclass


def agent(percepts, available_actions, previous_actions):
    """Handle one agent turn

    :param percepts: dictionary of current percepts (sensor data)
    :param previous_actions: List of all previous actions (most recent last)
    :param actions: List of valid actions
    
    Percept descriptions
    
    - "obstructed" will be True if the path forward is blocked
    - "facing" will be the current direction as one of ["n", "s", "e", "w"]
    - "temp" will be a value between 1 and 100. It will increase by
    1 on each move and decrease 1 on each rest.
    
    Action descriptions
    
    "forward" will move forward 1 space
    "left" will turn to the left
    "right" will turn to the right
    "rest" will do nothing. Temperature will decrease by 1

    Returns exactly one action from list of valid actions
    """
    
    pass

houses = [
    """
***
*.*
*.*
*.*
*.*
*.*
*.*
*.*
***
""",
    """
****
*..*
*..*
****
""",
    """
*****
*...*
*...*
*...*
*****
""",
    """
*********
*.......*
*.......*
*.......*
*.......*
*********
""",
    """
*********
*...*...*
*...*...*
**.**...*
*.......*
*********
""",
    """
*********
*...*...*
*...*...*
**.**...*
*.......*
*.......*
**.***.**
*.......*
*.......*
*********
""",
    """
*******************
*.*..*....*.......*
*....*....*.......*
*.*..*....*.......*
*.*****.***.......*
*.................*
*...*.....*********
*.........*.......*
*......*..........*
*.........*.......*
***.*******.......*
*.........*****.***
*.........*.......*
*.........*.......*
*******************
""",
]


class Board:
    def __init__(self, definition):
        """Converts string reprentation to 2d list

        >>> Board("***\\n*.*\\n*.*\\n***")
        [['*', '*', '*'], ['*', '.', '*'], ['*', '.', '*'], ['*', '*', '*']]
        """

        self.rows = [list(r) for r in definition.strip().split("\n")]

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
        directions = "nesw"

        direction = directions.index(self.name)
        direction = (direction + int(angle / 90)) % 4

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
            "n": (0, -1),
            "e": (1, 0),
            "s": (0, 1),
            "w": (-1, 0),
        }

        return (
            pos[0] + dist * directions[self.name][0],
            pos[1] + dist * directions[self.name][1],
        )

    def __str__(self):
        return self.name


def clean_house(house, agent, delay=0.5, limit=100000, allow_useless=True):
    house = Board(house)

    action = None
    pos = (1, 1)
    facing = Direction("s")
    temperature = 25

    house.set(pos, facing.name)
    
    previous_actions = []

    for i in range(limit):
        if delay > 0:
            print(f"Turn: {i} Temp: {temperature}")
            print(f"Completed action: {action}")
            for row in house.rows:
                print("".join(row))

            time.sleep(delay)

        if not house.contains("."):
            return i

        actions = ["left", "right", "rest"]

        if house.get(facing.move(pos)) != "*":
            actions.insert(0, "forward")
            
        percepts = {
            "facing": facing.name,
            "obstructed": "forward" not in actions,
            "temp": temperature,
        }

        action = agent(percepts, actions, previous_actions)
        previous_actions.append(action)

        if not allow_useless:
            assert action in actions
        else:
            if not action in actions:
                continue

        house.set(pos, " ")

        if action == "right":
            facing.turn_cw(90)
            temperature += 1
        elif action == "left":
            facing.turn_cw(-90)
            temperature += 1
        elif action == "forward":
            pos = facing.move(pos)
            temperature += 1
        elif action == "rest":
            temperature = max(temperature - 1, 25)
            
        if temperature >= 100:
            print("The vacuum is on fire (it should rest to keep temp under 100)")
            return float("inf")

        house.set(pos, facing.name)

    return float("inf")


if __name__ == "__main__":
    for i, house in enumerate(houses):
        if clean_house(house, agent, delay=0) < 100000:
            results = [clean_house(house, agent, delay=0) for i in range(100)]
            average = sum(results) / len(results)

            print(
                f"Cleaned house {i} in {average:.1f} seconds on average (max {max(results)})."
            )
        else:
            print(f"Took too long to clean house {i}")
            clean_house(house, agent, delay=0.5)
            break
