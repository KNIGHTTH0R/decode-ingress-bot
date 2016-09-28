"""Morse operations"""
from utils.functions import command


encoding = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.'
            }

decoding = dict((v, k) for (k, v) in encoding.items())

swapping = {'.': '-', '-': '.'}


@command("morse")
def encode(text):
    """Encode"""
    # should really pre-process {'.': 'stop', ',': 'comma', '-': 'dash', ...}
    return ' '.join(map(lambda x, g=encoding.get: g(x, ' '), text.upper()))


@command("demorse")
def decode(message):
    """Decode"""
    ans = ''.join(map(lambda x, g=decoding.get: g(x, ' '), message.split(' ')))
    return ' '.join(ans.split())  # tidy up spacing


@command("esrom")
def reverse(text):
    """Reverse Morse"""
    import tools.base as base
    return base.reverse(encode(text))


@command("m2b")
def morse_to_binary(code):
    """Morse to binary (.=0, -=1)"""
    if type(code) is str:
        return code.replace('.', '0').replace('-', '1')
    elif type(code) is list:
        return [morse_to_binary(c) for c in code]
    else:
        return code


@command("morseswap")
def swap(message):
    """Swap Morse"""
    return ''.join(map(lambda x: swapping.get(x, ' '), message))


def decipher(message):
    # like decode, but when there are no spaces.
    row = [('', message)]
    while filter(lambda x: x[1], row):
        old = row
        row = []
        for it in old:
            txt, code = it
            if code:
                for (t, c) in encoding.items():
                    if code[:len(c)] == c:
                        row.append((txt + t, code[len(c):]))
                        # NB we discard it if no initial segment of code matches an encoding.
            else: row.append(it)

    return map(lambda it: it[0], row)


@command("mrle")
def morse_rle(code):
    """Morse RLE: digits to .'s and chars to -'s"""
    def f(c):
        if c.isalpha():
            return '-' * (ord(c.lower()) - ord('a') + 1)
        elif c.isdigit():
            return '.' * int(c)
        else:
            return c

    return [f(c) for c in code]


@command("mtrans")
def morse_translate(code, dots, dashes):
    """Translate chars in 1st arg to .'s, chars in 2nd arg to -'s"""
    def trans(c, dots, dashes):
        if c in dots:
            return '.'
        elif c in dashes:
            return '-'
        else:
            return c

    def _inner(code, dots, dashes):
        if type(code) is str:
            return ''.join([trans(c, dots, dashes) for c in code])
        elif type(code) is list:
            return [_inner(row, dots, dashes) for row in code]
        else:
            return code

    return _inner(code, dots, dashes)
