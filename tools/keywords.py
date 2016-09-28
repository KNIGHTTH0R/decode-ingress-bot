"""Passcode keywords utils"""
from utils.functions import command
import re
import os

# https://raw.githubusercontent.com/ingresscodes/keywords/master/sorted.txt

path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(path, os.pardir, 'tools', 'raw', 'sorted.txt')) as f:
    keywords = [k.strip('\n') for k in f.readlines()]


@command("findkwd", store=False)
def find_keyword(code):
    """Find keyword"""
    if type(code) is str:
        s = "^[" + code.lower() + "]{" + str(len(code) - 10) + "}$"
        r = re.compile(s)
        return [kwd for kwd in keywords if r.match(kwd)]
    else:
        return code


@command("addkwd")
def insert_keyword(s, keyword):
    """Insert keyword"""
    if len(s) == 10:
        return s[:5] + keyword + s[5:]
    else:
        return s


@command("subkwd")
def replace_keyword(s, keyword):
    """Replace keyword"""
    if len(s) > 10:
        return s[:5] + keyword + s[-5:]
    else:
        return s
