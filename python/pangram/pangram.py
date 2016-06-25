from string import ascii_lowercase


def is_pangram(text):
    for letter in ascii_lowercase:
        if letter not in text.lower():
            return False
    else:
        return True
