"""Bifid utils"""
from utils.functions import command
import pycipher


@command("bifid")
def encode(s):
    """Encode"""
    return pycipher.Bifid(key='ABCDEFGHIKLMNOPQRSTUVWXYZ').encipher(s)


@command("debifid")
def decode(s):
    """Decode"""
    bifid = pycipher.Bifid(key='ABCDEFGHIKLMNOPQRSTUVWXYZ')
    bifid.period = len(s)
    return bifid.decipher(s.upper().replace('J', 'I'))
