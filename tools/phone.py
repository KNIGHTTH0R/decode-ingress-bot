"""Phone utils"""
from utils.functions import command

phone_map = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}

phone_map_reverse = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

@command("phone")
def phone_keyboard(code):
    """Letters to numbers"""
    if type(code) is str:
        return [phone_map.get(c.upper(), c) for c in code]
    elif type(code) is list:
        return [phone_keyboard(c) for c in code]


@command("enohp")
def phone_keyboard_reverse(code):
    """Numbers to letters: pairs of numbers to select letters"""
    if type(code) is str:
        try:
            if len(code) == 2 and 20 < int(code) < 95:
                return phone_map_reverse[code[0]][int(code[1]) - 1]
        except ValueError:
            return code
    elif type(code) is list:
        return [phone_keyboard_reverse(c) for c in code]


@command("t9")
def phone_keyboard_t9(code):
    """T9 transform"""
    if type(code) is str:
        return code
    elif type(code) is list and all(c.isdigit() for c in code) and all(c == c[0] * len(c) for c in code):
        return [phone_map_reverse[c[0]][len(c) - 1] for c in code]
    else:
        return code

