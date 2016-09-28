"""Leet Speak"""
from utils.functions import command


@command("leet")
def leet_speak(l):
    """Leet Speak"""
    leet_speak_map = {'1': 'l', '3': 'e', '0': 'o'}

    def _leet_speak(s):
        return ''.join([leet_speak_map.get(c, c) for c in s])

    if type(l) is list:
        return [_leet_speak(e) for e in l]
    else:
        # apply to keyword only
        return l[:5] + _leet_speak(l[5:-5]) + l[-5:]