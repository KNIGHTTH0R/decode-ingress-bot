"""Hex operations"""
from utils.functions import command
import binascii


@command("h2a")
def hex2ascii(s):
    """Hex to ASCII"""
    if type(s) is str:
        return binascii.unhexlify(s).decode()
    elif type(s) is list:
        return [hex2ascii(r) for r in s]
    else:
        return s


@command("a2h")
def ascii2hex(s):
    """ASCII to Hex"""
    if type(s) is str:
        return binascii.hexlify(str.encode(s)).decode()
    elif type(s) is list:
        return [ascii2hex(r) for r in s]
    else:
        return s
