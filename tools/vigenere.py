"""Vigenere cipher tools"""
from itertools import cycle
from functools import reduce
from utils.functions import command
import pycipher

ALPHA = 'abcdefghijklmnopqrstuvwxyz'


@command("vig")
def encrypt(plaintext, key):
    """Vigenere encode"""
    # Remove non-alpha chars
    pairs = zip(filter(str.isalpha, plaintext), cycle(key.lower()))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


@command("devig")
def decrypt(ciphertext, key):
    """Vigenere decode"""
    pairs = zip(filter(str.isalpha, ciphertext.lower()), cycle(key.lower()))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


@command("auto")
def encrypt_autokey(plaintext, key):
    """Vigenere autokey encode"""
    return pycipher.Autokey(key).encipher(plaintext)


@command("deauto")
def decrypt_autokey(ciphertext, key):
    """Vigenere autokey decode"""
    return pycipher.Autokey(key).decipher(ciphertext)