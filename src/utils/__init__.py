"""
==============================================================================
Project functionality utilities.
==============================================================================
"""

from enum import Enum
import sys


class Categories(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class StatusCode(Enum):
    SUCCESS = 0
    NO_DOTENV_KEYS = 1
    INVALID_ARGUMENTS = 2

    # Not reccomended to use a generic error. Better add a new status code error.
    GENERIC_ERROR = sys.maxsize
