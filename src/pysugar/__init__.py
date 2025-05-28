from functools import reduce, partial
from math import ceil, floor
from statistics import mean
from time import sleep
import sys

def efilter(*args, **kwargs):
    return list(filter(*args, **kwargs))

def emap(*args, **kwargs):
    return list(map(*args, **kwargs))

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
