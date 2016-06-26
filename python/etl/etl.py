"""
dict comprehension syntax figured out! (I put it opposite way previously).
Also - renamed vars to more meaningful names.
"""


def transform(data):
    return {item.lower(): score for score, items in data.items() for item in items}