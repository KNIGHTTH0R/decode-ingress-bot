"""Binary operations"""
from utils.functions import command


@command('binenc')
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    """Encode"""
    if type(text) is str:
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    elif type(text) is list:
        return [text_to_bits(t) for t in text]
    else:
        return text


@command('bindec')
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    """Decode"""
    if type(bits) is str:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    elif type(bits) is list:
        return [text_from_bits(b) for b in bits]
    else:
        return bits


@command("brle")
def binary_run_length_encoding(code):
    """Binary RLE"""
    if type(code) is str:
        if len(code) < 1:
            return code
        elif len(code) == 1:
            return '0' * int(code[0])
        elif len(code) == 2:
            return '0' * int(code[0]) + '1' * int(code[1])
        else:
            return binary_run_length_encoding(code[:2]) + binary_run_length_encoding(code[2:])
    elif type(code) is list:
        return [binary_run_length_encoding(e) for e in code]

