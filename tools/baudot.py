"""Baudot utils"""
from utils.functions import command

baudot_table = {
    '10111': 'Q',
    '10011': 'W',
    '00001': 'E',
    '01010': 'R',
    '10000': 'T',
    '10101': 'Y',
    '00111': 'U',
    '00110': 'I',
    '11000': 'O',
    '10110': 'P',
    '00011': 'A',
    '00101': 'S',
    '01001': 'D',
    '01101': 'F',
    '11010': 'G',
    '10100': 'H',
    '01011': 'J',
    '01111': 'K',
    '10010': 'L',
    '10001': 'Z',
    '11101': 'X',
    '01110': 'C',
    '11110': 'V',
    '11001': 'B',
    '01100': 'N',
    '11100': 'M'
}


@command("baudot")
def baudot_enc(s):
    """Baudot decode"""
    if all(c != '0' or c != '1' for c in s) and len(s) % 5 == 0:
        return ''.join(([baudot_table[s[i:i+5]] for i in range(0, len(s), 5)]))
    else:
        return s