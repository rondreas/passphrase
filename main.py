# py3

"""

    Passphrase generator

"""

from random import sample
from english_words import english_words_lower_set

def main():
    # exclude any word with fewer than 4 characters,
    words_set = [word for word in english_words_lower_set if 4 <= len(word)]

    # get a random sample from the set of words,
    words = sample(words_set, 4)
    print(''.join(map(lambda s: s.capitalize(), words)))

if __name__ == '__main__':
    main()
