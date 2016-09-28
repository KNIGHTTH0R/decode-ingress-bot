"""Braille utils"""
from utils.functions import command

braille_to_ascii_map = {
    (1,):  'A', (2,):  '1',
    (1,2): 'B', (2,3): '2',
    (1,4): 'C', (2,5): '3',
    (1,4,5): 'D', (2,5,6): '4',
    (1,5): 'E', (2,6): '5',
    (1,2,4): 'F', (2,3,5): '6',
    (1,2,4,5): 'G', (2,3,5,6): '7',
    (1,2,5): 'H', (2,3,6): '8',
    (2,4): 'I', (3,5): '9',
    (2,4,5): 'J', (3,5,6): '0',
    (1,3): 'K',
    (1,2,3): 'L',
    (1,3,4): 'M',
    (1,3,4,5): 'N',
    (1,3,5): 'O',
    (1,2,3,4): 'P',
    (1,2,3,4,5): 'Q',
    (1,2,3,5): 'R',
    (2,3,4): 'S',
    (2,3,4,5): 'T',
    (1,3,6): 'U',
    (1,2,3,6): 'V',
    (2,4,5,6): 'W',
    (1,3,4,6): 'X',
    (1,3,4,5,6): 'Y',
    (1,3,5,6): 'Z'
}

@command("m2b2a")
def morse_2_braille_2_ascii(code):
    """Morse to Braille to ASCII"""
    if type(code) is list \
        and all(len(e) == 6 for e in code) \
        and all((all(c == '.' or c == '-' for c in e)) for e in code):
        return ''.join([braille_to_ascii_map[tuple([i+1 for i, v in enumerate(list(e)) if v == '-'])] for e in code])
    else:
        return code