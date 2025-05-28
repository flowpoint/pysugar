from functools import reduce, partial
from math import ceil, floor
from statistics import mean

def efilter(*args, **kwargs):
    return list(filter(*args, **kwargs))

def emap(*args, **kwargs):
    return list(map(*args, **kwargs))
