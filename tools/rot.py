"""ROT-n utils"""
from utils.functions import command
import string


@command("rots", store=False)
def rotall(s):
    """ROT n from 1 to 25"""
    return [str(i) + ": " + rot(s, i) for i in range(1, 26)]


@command("stor", store=False)
def torall(s):
    """ROT -n from 1 to 25"""
    return [str(-i) + ": " + invrot(s, i) for i in range(1, 26)]


@command("rot")
def rot(s, n=13):
    """ROT n (default n=13)"""
    n = int(n)
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    digits_start = ord(digits[0])

    def _rot_c(c, n, s, l):
        return chr(s + (ord(c) - s + n) % l)

    out = ''
    for c in s:
        if c in upper:
            out += _rot_c(c, n, upper_start, len(upper))
        elif c in lower:
            out += _rot_c(c, n, lower_start, len(lower))
        elif c in digits:
            out += _rot_c(c, n, digits_start, len(digits))
        else:
            out += c
    return out


@command("tor")
def invrot(s, n=13):
    """ROT -n (default n=13)"""
    n = int(n)
    return rot(s, -n)


def _rot_wave(code, n):
    signs = [1, -1]
    return "".join([rot(c, signs[(i % 2)] * int(n)) for i, c in enumerate(code)])


@command("rotwave")
def rot_wave(code, n=13):
    """Alternate ROT -n/+n and ROT +n/-n (order depends on provided n's sign)"""
    return _rot_wave(code, int(n))
