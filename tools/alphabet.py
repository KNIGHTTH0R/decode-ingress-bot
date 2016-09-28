"""Alphabet utils"""
from utils.functions import command
alphabet = 'abcdefghijklmnopqrstuvwxyz'


@command("d2a")
def decimal_to_letters(l):
    """Decimal to ASCII"""
    if type(l) is list:
        r = [chr(int(d)) for d in l]
        return r if all(c.isalnum() for c in r) else l
    else:
        return l


def _letters_to_numbers(code, f):
    def _f(c):
        return c if c.isdigit() else str(f(c))

    if type(code) is str:
        return "".join([_f(c) for c in code])
    elif type(code) is list:
        return [_letters_to_numbers(c, f) for c in code]


@command("a0z25")
def a0z25(code):
    """a=0 ... z=25"""
    return _letters_to_numbers(code, lambda c: ord(c.lower()) - ord('a'))


@command("a25z0")
def a25z0(code):
    """a=25 ... z=0"""
    return _letters_to_numbers(code, lambda c: ord('z') - ord(c.lower()))


@command("a1z26")
def a1z26(code):
    """a=1 ... z=26"""
    return _letters_to_numbers(code, lambda c: ord(c.lower()) - ord('a') + 1)


@command("a26z1")
def a26z1(code):
    """a=26 ... z=1"""
    return _letters_to_numbers(code, lambda c: ord('z') - ord(c.lower()) + 1)


# Numbers to letters
def _numbers_to_letters(code, f):
    if type(code) is str:
        return alphabet[f(code)]
    elif type(code) is list:
        return [_numbers_to_letters(c, f) for c in code]


@command("0a25z")
def zero_a25z(code):
    """0=a ... 25=z"""
    return _numbers_to_letters(code, lambda c: int(c))


@command("1a26z")
def one_a26z(code):
    """1=a ... 26=z"""
    return _numbers_to_letters(code, lambda c: int(c) - 1)


@command("25a0z")
def tf_a0z(code):
    """25=a ... 0=z"""
    return _numbers_to_letters(code, lambda c: -1 * (int(c) + 1))


@command("26a1z")
def ts_z25a(code):
    """26=a ... 1=z"""
    return _numbers_to_letters(code, lambda c: -1 * int(c))


@command("highlow")
def high_low(code):
    if type(code) is str:
        code = 'a' + code
        return ''.join([_higher_lower_equal(code[i], code[i+1]) for i in range(0, len(code)-1)])
    else:
        return code


def _higher_lower_equal(a, b):
    if a == b:
        return ' '
    elif a < b:
        return '1'
    else:
        return '0'
