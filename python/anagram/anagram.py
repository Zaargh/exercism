from collections import Counter


def detect_anagrams(word, candidates):
    return [c for c in candidates
            if Counter(c.lower()) == Counter(word.lower())
            if c.lower() != word.lower()]
