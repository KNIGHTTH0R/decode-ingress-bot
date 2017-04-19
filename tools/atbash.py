"""Atbash utils"""
from utils.functions import command


def atbash_c(c):
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        lower = (ord('a'), ord('z'))
        upper = (ord('A'), ord('Z'))
        limits = upper if ord(c) < lower[0] else lower
        return chr(limits[1] - ((ord(c) + (limits[1] - limits[0])) % limits[1]))
    else:
        return c


def atbash_n(n, lower='1'):
    if lower <= n <= '9':
        limits = (ord(lower), ord('9'))
        return chr(limits[1] - ((ord(n) + (limits[1] - limits[0])) % limits[1]))
    else:
        return n


@command("atbash")
def atbash(s):
    """Encode"""
    return atbash_main(s)


@command("atbashnum")
def atbash_num(s):
    """Encode letters and numbers"""
    return atbash_main(s, numeric=True)


@command("atbashnumz")
def atbash_numz(s):
    """Encode letters and numbers (incl. zero)"""
    return atbash_main(s, numeric=True, zero=True)


hex_alphabet = '0123456789ABCDEF'
atbashhex = dict([(v, hex_alphabet[-1 * (k + 1)]) for k, v in enumerate(list(hex_alphabet))])


@command("atbashhex")
def atbash_hex(s):
    """Hex"""
    if type(s) is list:
        return [atbash_hex(t) for t in s]
    return ''.join([atbashhex[c.upper()] for c in s])


def atbash_main(s, numeric=False, zero=False):
    result = ""
    lower = '0' if zero else '1'
    for c in s:
        if c.isalpha():
            result += atbash_c(c)
        elif c.isnumeric():
            result += atbash_n(c, lower) if numeric else c
        else:
            result += c
    return result

