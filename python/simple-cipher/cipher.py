import random

from string import ascii_lowercase
from itertools import cycle


class Caesar:

    @staticmethod
    def encode(text, alphabet=ascii_lowercase, shift=3):
        text = ''.join(letter for letter in text.lower() if letter in alphabet)
        return ''.join(alphabet[(alphabet.index(letter) + shift) % len(alphabet)] for letter in text)

    @staticmethod
    def decode(text, alphabet=ascii_lowercase, shift=3):
        return ''.join(alphabet[(alphabet.index(letter) - shift) % len(alphabet)] for letter in text)


class Cipher:

    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(ascii_lowercase) for i in range(512))
        elif key.islower() and key.isalpha():
            self.key = key
        else:
            raise ValueError

    def encode(self, text, alphabet=ascii_lowercase):
        text = ''.join(letter for letter in text.lower() if letter in alphabet)
        crypt = zip(text, cycle(alphabet.index(letter) for letter in self.key))
        return ''.join(alphabet[(alphabet.index(letter) + shift) % len(alphabet)] for letter, shift in crypt)

    def decode(self, text, alphabet=ascii_lowercase):
        crypt = zip(text, cycle(alphabet.index(letter) for letter in self.key))
        return ''.join(alphabet[(alphabet.index(letter) - shift) % len(alphabet)] for letter, shift in crypt)
