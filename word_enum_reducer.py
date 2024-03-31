#!/usr/bin/env python

import sys

def word_enum_reducer():
    current_word = None
    word_count = 0
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        count = int(count)
        if current_word == word:
            word_count += count
        else:
            if current_word:
                print(f"{current_word}\t{word_count}")
            current_word = word
            word_count = count
    if current_word:
        print(f"{current_word}\t{word_count}")

if __name__ == "__main__":
    word_enum_reducer()