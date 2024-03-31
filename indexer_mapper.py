#!/usr/bin/env python

import sys
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def indexer_mapper():
    for line in sys.stdin:
        data = line.strip().split(',')
        if len(data) < 4:
            # Skip lines with insufficient data
            continue
        article_id = data[0]
        section_text = data[3]  # Assuming 'SECTION_TEXT' is at index 3
        words = word_tokenize(section_text.lower())
        word_count = len(words)
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        for word, freq in word_freq.items():
            tf = freq / word_count
            print(f"{word}\t{article_id},{tf}")

if __name__ == "__main__":
    indexer_mapper()

