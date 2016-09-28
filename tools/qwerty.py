"""QWERTY utils"""
from utils.functions import command

# s2n_dict = {'!': 1, '"': 2, '£': 3, '$': 4, '%': 5, '&': 6, '/': 7, '(': 8, ')': 9, '=': 0}
s2n_dict = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}

n2s_dict = dict((v, k) for (k, v) in s2n_dict.items())

ext_qwerty_layout = [
    '1234567890',
    'qwertyuiop',
    'asdfghjkl;',
    'zxcvbnm,./'
]

qwerty_layout = [
    'qwertyuiop',
    'asdfghjkl;',
    'zxcvbnm,./'
]


@command("qs2n")
def symbol_to_number(s):
    """QWERTY symbol to number"""
    if type(s) is str:
        return ''.join([s2n_dict.get(i, i) for i in s])
    else:
        return [symbol_to_number(e) for e in s]


@command("qmirror")
def qwerty_mirror(code):
    """QWERTY mirror"""
    if type(code) is str:
        res = []
        for c in code:
            for row in qwerty_layout:
                try:
                    i = row.index(c)
                    res.append(row[-1 * (i+1)])
                    break
                except ValueError:
                    continue
        if len(res) < len(code):
            res = code
        return "".join(res)
    else:
        return [ext_qwerty_layout(c) for c in code]


@command("qnums")
def qwerty_columns(code):
    """Chars to column-wise digits"""
    if type(code) is str:
        res = ''
        for c in code:
            for i, row in enumerate(qwerty_layout):
                if c in row:
                    res += str((row.index(c) + 1) % 10)
                    break
        if len(res) < len(code):
            res = code
        return res


@command("qmatrix")
def qwerty_matrix(code):
    """Numbers to qwerty char"""
    if type(code) is list:
        if all(c.isnumeric() for c in code) and all(c == len(c) * c[0] for c in code):
            return [qwerty_layout[len(c)-1][int(c[0])-1] for c in code]
        else:
            return code
    else:
        return code


keypad_table = {
    '1': '7', '2': '8', '3': '9', 'q': '4',	'w': '5', 'e': '6', 'a': '1', 's': '2', 'd': '3', 'x': '0'
}


@command("keypad")
def keypad_decode(code):
    """Qwerty to num keypad"""
    return ''.join([keypad_table[c] for c in code])

