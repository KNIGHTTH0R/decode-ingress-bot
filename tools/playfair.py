"""Playfair utils"""
from utils.functions import command
from pycipher import Playfair


@command("playfair")
def playfair_decode(s):
    """Decode"""
    return Playfair().decipher(s)
