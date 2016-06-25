from itertools import groupby
import re


def remove_ones(pair):
    if pair[0] == '1':
        return ('', pair[1])
    return pair


def encode(text):
    counted_occurences = [(str(len(list(g))), k) for k, g in groupby(text)]
    cleaned = [remove_ones(x) for x in counted_occurences]
    return ''.join([''.join(x) for x in cleaned])


def decode_pair(pair):
    if pair[0] != '':
        count = re.findall('[0-9]+', pair[0])[0]
        return pair[0][-1] * int(count)
    else:
        return pair[1]


def decode(code):
    r = re.compile('([0-9]+\D)|(\D)')
    parts = r.findall(code)
    return ''.join((decode_pair(pair) for pair in parts))
