"""Roman numbers operations"""
from utils.functions import command
import roman


@command("roman")
def roman_decode(code):
    """Convert roman numbers"""
    if type(code) is not list:
        return code
    else:
        return [str(roman.fromRoman(n.upper())) for n in code]

