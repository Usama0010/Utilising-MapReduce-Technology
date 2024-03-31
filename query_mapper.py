#!/usr/bin/env python

import sys
from nltk.tokenize import word_tokenize

def query_mapper():
    for line in sys.stdin:
        words = word_tokenize(line.strip().lower())
        for word in words:
            print(f"{word}\tquery")

if __name__ == "__main__":
    query_mapper()

