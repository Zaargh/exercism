import num2words    # A little bit of cheating :)


def say(n):
    if n < 0 or n >= 1e12:
        raise AttributeError
    return num2words.num2words(n, lang='en').replace(',', '')
