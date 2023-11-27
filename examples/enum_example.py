"""How to have constants in Python."""

from enum import Enum, auto, StrEnum


class Color(StrEnum):
    """Color constants."""
    RED = auto()
    GREEN = auto()
    BLUE = auto()


if __name__ == '__main__':
    # example usage
    print(Color.RED)
    print(Color.GREEN)
    print(Color.BLUE)
    if Color.RED == 'red':
        print('RED is RED')
