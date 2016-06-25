from string import ascii_lowercase, digits
import re


ATBASH_KEY = dict(zip(ascii_lowercase + digits,
                      ascii_lowercase[::-1] + digits))


def encode(text):
    text = ''.join(re.findall('[a-z0-9]', text.lower()))
    encoded = ''.join(ATBASH_KEY[c] for c in text)
    encoded = ' '.join(re.findall('.{1,5}', encoded))
    return encoded


def decode(text):
    text = ''.join(re.findall('[a-z0-9]', text.lower()))
    decoded = ''.join(ATBASH_KEY[c] for c in text)
    return decoded
