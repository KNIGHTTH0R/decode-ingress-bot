"""Base64 (and 32, 16) operations"""
import base64
from utils.functions import command

base64_index_table = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
    26: 'a',
    27: 'b',
    28: 'c',
    29: 'd',
    30: 'e',
    31: 'f',
    32: 'g',
    33: 'h',
    34: 'i',
    35: 'j',
    36: 'k',
    37: 'l',
    38: 'm',
    39: 'n',
    40: 'o',
    41: 'p',
    42: 'q',
    43: 'r',
    44: 's',
    45: 't',
    46: 'u',
    47: 'v',
    48: 'w',
    49: 'x',
    50: 'y',
    51: 'z',
    52: '0',
    53: '1',
    54: '2',
    55: '3',
    56: '4',
    57: '5',
    58: '6',
    59: '7',
    60: '8',
    61: '9',
    62: '+',
    63: '/'
}


@command("b64table")
def b64table(code):
    """Index table"""
    if type(code) is list and all(len(c) == 2 and int(c) for c in code):
        return [base64_index_table.get(int(c), c) for c in code]
    else:
        return code


@command("b64enc")
def b64encode(s):
    """Encode"""
    return base64.b64encode(str.encode(s)).decode()


@command("b64dec")
def b64decode(s):
    """Decode"""
    return base64.b64decode(str.encode(s)).decode()


@command("b32enc")
def b32encode(s):
    """Encode"""
    return base64.b32encode(str.encode(s)).decode()


@command("b32dec")
def b32decode(s):
    """Decode"""
    return base64.b32decode(str.encode(s)).decode()


@command("b16enc")
def b16encode(s):
    """Encode"""
    return base64.b16encode(str.encode(s)).decode()


@command("b16dec")
def b16decode(s):
    """Decode"""
    return base64.b16decode(str.encode(s)).decode()
