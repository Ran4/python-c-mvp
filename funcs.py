import os
from ctypes import CDLL

BASE_PATH: str = os.path.dirname(os.path.abspath(__file__))

__funcs_so = CDLL(os.path.join(BASE_PATH, "c_funcs.so"))

# Let's try to get the attributes so that we'll crash as quickly as possible
# if they're missing from the .so file
__square = __funcs_so.square


# We wrap all the calls in order to add our own docstrings, or own validation
# and so on

def square(number: int):
    """
    Square func
    """
    return __square(number)
