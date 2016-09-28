"""Rectangles operations"""
from utils.functions import command


def reverse(s):
    """Reverse string or flip rectangle"""
    return s[::-1]


@command("rar")
def reverse_all(l):
    """Reverse all rows"""
    return [reverse(s) for s in l]


@command("rer")
def reverse_even_rows(l):
    """Reverse even rows (first is 0)"""
    return reverse_rows(l, odd=False, even=True)


@command("ror")
def reverse_odd_rows(l):
    """Reverse odd rows"""
    return reverse_rows(l, odd=True, even=False)


def reverse_rows(l, odd=False, even=False):
    result = []
    for k, v in enumerate(l):
        if k % 2 == 0:
            result.append(reverse(v) if even else v)
        else:
            result.append(reverse(v) if odd else v)
    return result


@command("readcols")
def read_columns(l):
    """Read columns"""
    n = len(l[0])
    result = ""
    for i in range(0, n):
        for e in l:
            result += e[i]
    return result


@command("join")
def join(v):
    """Read rows"""
    if type(v) is list:
        return ''.join(v)
    else:
        return v


@command('joinspace')
def print_row(l):
    """Join rows w/ spaces"""
    if type(l) is list:
        return " ".join(l)
    else:
        return l


@command("trans")
def transpose(l):
    """Transpose rect"""
    if type(l) is list:
        return list(map(''.join,zip(*l)))
    else:
        return l


@command("rect")
def columns(s, n):
    """nxm rect"""
    offset = int(n)
    return [s[i:i+offset] for i in range(0, len(s), offset)]


@command("rects", store=False)
def columnise(s):
    """All nxm rects"""
    columns = []
    l = len(s)
    if l > 2:
        for n in range(2, l):
            if l % n == 0:
                columns.append([str(n) + "\n"] + [s[i:i+n] for i in range(0, l, n)])

    if len(columns) == 0:
        return s
    return columns


@command("takecol")
def select_column(l, i):
    """Take n-th column"""
    return "".join([e[int(i)] for e in l])


@command("shiftcol")
def shift_column(code, n, s):
    """Shift n-th column s positions down"""
    def shift(s, n):
        if n == 0 or len(s) == 1:
            return s
        else:
            return shift(s[-1] + s[:-1], n-1)

    if type(code) is not list:
        return code
    else:
        n = int(n)
        s = int(s) % len(code)
        if s > 0 and n < len(code[0]):
            column = select_column(code, n)
            column = shift(column, s)
            for i in range(0, len(column)):
                new = list(code[i])
                new[n] = column[i]
                code[i] = ''.join(new)
            return code
        else:
            return code


@command("group")
def group_columns(code, offset):
    """Group columns by n"""
    if type(code) is str:
        return code
    elif type(code) is list and len(code) > 0:
        offset = int(offset)
        if len(code[0]) % offset != 0:
            return code
        else:
            r = []
            for i in range(0, len(code[0]), offset):
                r.append(''.join([row[i: i+offset] for row in code]))
            return r
    else:
        return code


