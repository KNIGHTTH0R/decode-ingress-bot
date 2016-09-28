"""Railfence utils"""
from utils.functions import command
import pycipher


@command("enfence")
def railfence_encode(code, fences=3):
    """Railfence encode (default 3)"""
    railfence = pycipher.Railfence(key=int(fences))
    return railfence.encipher(code, keep_punct=True)


@command("defence")
def railfence_decode(code, fences=3):
    """Railfence decode (default 3)"""
    railfence = pycipher.Railfence(key=int(fences))
    return railfence.decipher(code, keep_punct=True)