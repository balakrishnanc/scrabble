#!/usr/bin/env python3
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
"""Search for valid English words using the given letters.
"""

import argparse
import gzip
from itertools import chain, combinations, permutations
import sys


def mk_guesses(letters, min_len):
    """Given a sequence of `letters`, permute the letters in different words to
    guess all possible words of length at least equal to `min_len`.
    """
    # Possible word lengths
    word_lengths = (n for n in range(min_len, len(letters) + 1))
    # Letter combinations.
    choices = (combinations(letters, i) for i in word_lengths)
    # Guess words from letter combinations.
    guesses = (permutations(w) for w in chain(*choices))
    return (''.join(w) for w in chain(*guesses))


def load_dict(dict_file):
    """Load dictionary from plain text file."""
    with gzip.open(dict_file, 'rt') as df:
        return {word.strip() for word in df}


def filter_words(words, dictionary):
    """Filter out words not in dictionary."""
    return {word for word in words if word in dictionary}


def main(args):
    dictionary = load_dict(args.dict_file)
    guesses = mk_guesses(args.letters, args.min_len)
    for word in filter_words(guesses, dictionary):
        print(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Retrieve proper words from the given letters")
    parser.add_argument('letters',
                        metavar='letters',
                        type=str,
                        help='Letters (without any space in between them)')
    parser.add_argument('--min-len', '-m',
                        dest='min_len',
                        metavar='min_len',
                        type=int,
                        default=3,
                        help='Minimum length of words')
    parser.add_argument('--dict', '-d',
                        dest='dict_file',
                        metavar='dict_file',
                        type=str,
                        default='corpus.txt.gz',
                        help='Compressed dictionary')
    main(parser.parse_args())
