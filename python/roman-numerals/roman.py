import collections


NUMERALS = collections.OrderedDict(sorted({
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}.items(), key=lambda t: t[0], reverse=True))


def numeral(arabic):
    if type(arabic) != type(1):
        raise AttributeError('Expected int, got {}'.format(type(arabic)))
    if not 0 < arabic < 4000:
        raise ValueError('Argument must be between 1 and 3999')

    answer = ''
    for k, v in NUMERALS.items():
        count = arabic // k
        answer += v * count
        arabic -= k * count

    return answer
