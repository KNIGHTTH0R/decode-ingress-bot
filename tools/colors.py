"""Colors utils"""
from utils.functions import command
from tools.raw.colors import hex2names
from itertools import product


@command("rgb2names", store=False)
def rgb2names(code):
    """RGB codes to color names"""
    if type(code) is not list:
        return code
    elif len(code) % 3 != 0:
        return code
    else:
        rgbs = ['#%02x%02x%02x' % tuple(map(int, code[i:i+3])) for i in range(0, len(code), 3)]
        comb = ["".join(set(map(lambda x: x[0], hex2names[rgb]))) for rgb in rgbs]
        return ["".join(c) for c in product(*comb)]
