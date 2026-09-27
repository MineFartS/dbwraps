from typing import Literal

names = Literal[
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'WHITE',
    'DEFAULT',
    'BOLD',
    'GRAY'
]
"""Type hint for keys in Color.values"""

values: dict[names, str] = {
    'BLACK' : '\033[30m',
    'RED' : '\033[31m',
    'GREEN' : '\033[32m',
    'YELLOW' : '\033[33m',
    'BLUE' : '\033[34m',
    'MAGENTA' : '\033[35m',
    'CYAN' : '\033[36m',
    'WHITE' : '\033[37m',
    'DEFAULT' : '\033[0m',
    'BOLD': '\033[1m',
    'GRAY': '\033[90m'
}
r"""
COLOR CONVERSION TABLE

EXAMPLE:
colors.values['RED'] -> '\033[31m'
"""

