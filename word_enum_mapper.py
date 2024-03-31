#!/usr/bin/env python

import sys
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def word_enum_mapper():
    for line in sys.stdin:
        words = word_tokenize(line.strip())
        for word in words:
            print(f"{word}\t1")

if __name__ == "__main__":
    word_enum_mapper()