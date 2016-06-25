"""
Just adding comment to iteration 2.
Using regex module instead of standard re because of \p{Unicode_property}
syntax. It allows creation of non-ASCII acronyms.
"""

import regex as re
from itertools import chain


def abbreviate(text):
    acronym_re = re.compile(r"""^(.)| # first character
                            \W(\w)|   # any alphanumeric after non-alphanumeric
                            \p{Ll}(\p{Lu})   # Uppercase letter after lowercase
                            """,
                            re.X)
    return ''.join(chain.from_iterable(acronym_re.findall(text))).upper()
