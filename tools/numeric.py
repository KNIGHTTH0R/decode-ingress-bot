"""Numerical utils"""
from utils.functions import command
import itertools


@command("roots")
def roots(code):
    """nth-root, roots('3433') = 3-root(343) = 7"""
    if type(code) is list:
        return [str(nroot(
            int(c[-1]),
            int(c[:-1]))
        ) + c[-1] for c in code]
    else:
        return str(nroot(
            int(code[-1]),
            int(code[:-1]))) + code[-1]


def nroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s


@command("plusminus")
def plus_minus(code):
    """Alternate sum and sub"""
    if type(code) is not list:
        return code
    else:
        pre = 0
        res = []
        for i, c in enumerate(code):
            curr = int(c)
            op = 1 if i % 2 == 0 else -1
            res.append(str(curr + (pre * op)))
            pre = int(res[i])
        return res


@command("acc")
def accumulate(code):
    """Accumulate numbers, e.g. +3 -2 +10 > 3 1 11"""
    if type(code) is not list:
        return code
    else:
        return [str(i) for i in itertools.accumulate([int(n) for n in code])]

