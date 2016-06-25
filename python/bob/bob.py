#
# Skeleton file for the Python "Bob" exercise.
#
import unicodedata as ud


def hey(what):
    what = what.rstrip()
    if what == '':
        return 'Fine. Be that way!'
    if what.isupper():
        return 'Whoa, chill out!'
    if what.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
