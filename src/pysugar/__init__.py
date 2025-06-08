from functools import reduce, partial
from itertools import accumulate
from more_itertools import flatten, chunked
from math import ceil, floor
from statistics import mean
from time import sleep
import sys

from copy import copy

def efilter(*args, **kwargs):
    ''' eager filter '''
    return list(filter(*args, **kwargs))

def emap(*args, **kwargs):
    ''' eager map '''
    return list(map(*args, **kwargs))

def eprint(*args, **kwargs):
    ''' print to stderr '''
    print(*args, file=sys.stderr, **kwargs)

def dpop(k, d):
    ''' returns copy of dict without an certain key '''
    d2 = copy(d)
    d2.pop(k, None)
    return d2
