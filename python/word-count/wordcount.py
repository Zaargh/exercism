import unicodedata as ud


def word_count(sentence):
    for ch in set(sentence):
        if ud.category(ch) not in ('Ll', 'Lu', 'Nd'):
            sentence = sentence.replace(ch, ' ')
    words = sentence.lower().split()
    return {key: words.count(key) for key in set(words)}
