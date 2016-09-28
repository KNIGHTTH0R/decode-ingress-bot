"""Basic operations"""
from utils.functions import command
import re
from tools.rectangles import columns, select_column
from tools.keywords import keywords


def select_column(l, i):
    """Take n-th column"""
    return "".join([e[int(i)] for e in l])


def columns(s, n):
    """Make a nxm rectangle"""
    offset = int(n)
    return [s[i:i+offset] for i in range(0, len(s), offset)]


@command("rev")
def reverse(s):
    """Reverse string/flip rect"""
    return s[::-1]


@command("revw")
def reverse_wings(code):
    """Reverse string edges"""
    if type(code) is str:
        if len(code) % 2 == 1:
            middle = int(len(code) / 2)
            return reverse(code[:middle]) + code[middle] + reverse(code[middle+1:])
        else:
            return code
    elif type(code) is list:
        return [reverse_wings(e) for e in code]
    else:
        return code


@command("sort")
def sort_rows(l):
    """Alphabetically"""
    return sorted(l)


@command("spiral")
def spiral(code):
    """Read rect in a spiral, top-left going right"""
    if type(code) is not list:
        return code
    elif not all(len(c) == len(code) for c in code):
        return code
    elif len(code) == 1:
        return code
    elif len(code) == 0:
        return ''
    else:
        # read external rectangle
        return ''.join([
            code[0],
            select_column(code, len(code) - 1)[1:],
            reverse(code[-1])[1:],
            reverse(select_column(code, 0)[1:-1])
        ]) + spiral([c[1:-1] for c in code[1:-1]])


def print_columns(l):
    print("\n".join(l))


@command("len", store=False)
def size(v):
    """Size of string/rect"""
    if type(v) is list:
        return len(''.join(v))
    else:
        return len(v)


@command("lenc", store=False)
def size_chars(v):
    """Size of string/rect w/o spaces"""
    if type(v) is list:
        return size_chars(''.join(v))
    else:
        return len(''.join(c for c in v if c != ' '))


@command("zigzag")
def zig_zag(s, lr=1):
    """Read string right-to-left starting from center"""
    lr = int(lr)
    if len(s) % 2 == 1:
        result = ""
        i = int(len(s) / 2)
        n = 1
        while i != 0:
            result += s[i]
            i += n * lr
            lr *= -1
            n += 1
        result += s[0]
        return result
    else:
        return s


@command("esac")
def reverse_case(code):
    """Swap case"""
    if type(code) is str:
        return code.swapcase()
    elif type(code) is list:
        return [reverse_case(c) for c in code]
    else:
        return code


@command("sum", store=False)
def sum_all(code):
    """Sum all digits"""
    return sum(int(digit) for digit in "".join(code) if digit.isdigit())


def sum_values(l):
    return [sum([int(i) for i in list(e)]) for e in l]


def sum_pairs(l):
    def _sum_pairs(p):
        return sum([int(i) for i in columns(p, 2)])
    return [_sum_pairs(e) for e in l]


@command("abbrv")
def abbreviate(s, n=2):
    """Numeric abbreviations (n=2..5 uses first 2..5 letters, natural abbrv otherwise)"""
    n = int(n)
    if type(s) is list:
        s = "".join(s)
    result = s.lower()
    natural = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if 2 <= n <= 5:
        table = dict((k[:n], v) for (k, v) in natural.items() if len(k) >= n)
    else:
        table = natural
    for (k, v) in table.items():
        result = result.replace(k, str(v))

    return result


@command("xabbrv")
def ext_abbreviate(s, n=2):
    """Extended numeric abbreviations (incl. 0 and 1)"""
    n = int(n)
    if type(s) is list:
        s = "".join(s)
    result = s.lower()
    natural = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if 2 <= n <= 5:
        table = dict((k[:n], v) for (k, v) in natural.items() if len(k) >= n)
    else:
        table = natural
    for (k, v) in table.items():
        result = result.replace(k, str(v))

    return result


@command("splitspace")
def split_space(s):
    """Split at spaces"""
    if type(s) is str:
        return s.split()
    else:
        return s


@command("split")
def split(s, c):
    """Split at character c (removing c)"""
    if type(s) is str:
        return s.split(c)
    else:
        return s


@command("splitat")
def split_at_char(code, c):
    """Split in pieces starting with c"""
    if type(code) is list:
        return code
    elif type(code) is str:
        pattern = "[%s][^%s]*" % (c, c)
        return re.findall(pattern, code)


@command("splitkeep")
def split_keep(code, c):
    """Split at char c (keep c)"""

    if type(code) is str:
        splits = code.split(c)
        r = []
        for s in splits[:-1]:
            if s != '':
                r.append(s)
            r.append(c)
        return r + ([splits[-1]] if splits[-1] != '' else [])
    else:
        return code


@command("splitupper")
def split_uppercase(s):
    """Split at uppercase letters"""
    if type(s) is str:
        return re.findall('[A-Z][^A-Z]*', s)
    elif type(s) is list:
        return [split_uppercase(c) for c in s]


@command("drange")
def decimal_range(code):
    """Split into ASCII decimal range"""
    if type(code) is not str:
        return code
    else:
        result = []
        acc = ''
        for c in code:
            acc += c
            if chr(int(acc)).isalnum():
                result.append(acc)
                acc = ''
        return result


@command("takenum")
def take_numbers(code):
    """Take digits"""
    return "".join([c for c in code if c.isdigit()])


@command("takealpha")
def take_alphas(code):
    """Take chars"""
    return "".join([c for c in code if c.isalpha()])


@command("skip")
def skip(code, n):
    """Skip n chars"""
    if type(code) is list:
        return code

    n = int(n) % len(code)
    if n < 2:
        return code
    else:
        return "".join([code[i] for offset in range(0, n) for i in range(offset, len(code), n)])


@command("skips", store=False)
def skips(code):
    """Skips from 2...len(code)"""
    if type(code) is list:
        return code

    if len(code) < 3:
        return code

    return ["%s: %s" % (str(n), skip(code, n)) for n in range(2, len(code))]


@command("elr")
def rle_decode(code):
    """Reverse RLE: consecutive repetitions of chars"""
    if type(code) is not str:
        return code
    else:
        current = ''
        num = 0
        result = ''
        for c in code:
            if c != current:
                if current != '' and num > 0:
                    result += str(num)
                current = c
                num = 1
            else:
                num += 1
        return result + str(num)


@command("repl")
def replace_c(code, c, r):
    """Replace c with r"""
    if type(code) is str:
        return code.replace(c, r)
    else:
        return [n.replace(c, r) for n in code]


@command("check", store=False)
def check(code):
    """Check valid passcode"""
    if type(code) is str:
        # split code
        c = code.lower()
        l = len(c)
        prefix = c[0:5]
        kwd = c[5:l-5]
        suffix = c[5 + len(kwd):]
        prefix_re = r"[2-9][a-z]{3}[2-9]"
        suffix_re = r"[a-z][2-9][a-z][2-9][a-z]"
        return "Valid passcode" if \
            re.match(prefix_re, prefix) is not None and re.match(suffix_re, suffix) is not None and kwd in keywords \
            else "Not a valid passcode"
    else:
        return "Not a valid passcode"
