"""Polybius square utils"""
from utils.functions import command
import pycipher.polybius


alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


@command("pbenc")
def polybius_encode(code):
    """Polybius square encode"""
    if type(code) is not str:
        return code
    else:
        cipher = pycipher.polybius.PolybiusSquare()
        return cipher.encipher(code)


@command("pbdec")
def polybius_decode(code):
    """Polybius square decode"""
    if type(code) is not str:
        return code
    elif all(c.isdigit() and 0 < int(c) < 6 for c in code):
        return ''.join([_decode_pair(code[i:i+2]) for i in range(0, len(code), 2)])
    else:
        return code


def _decode_pair(pair):
    row = int(pair[0]) - 1
    col = int(pair[1]) - 1
    return alphabet[row * 5 + col]
