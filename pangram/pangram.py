import string


def is_pangram(sentence):
    return len(set(sentence)) > 26
