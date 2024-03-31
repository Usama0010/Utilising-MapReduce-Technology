#!/usr/bin/env python

import sys
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def doc_count_mapper():
    for line in sys.stdin:
        words = line.strip().split(',')
        if len(words) >= 4:  # Ensure at least 4 fields are present
            article_id = words[0]
            section_text = words[3]
            unique_words = set(word_tokenize(section_text.lower()))
            for word in unique_words:
                print(f"{word}\t{article_id}")
        else:
            # Handle lines with insufficient fields
            sys.stderr.write("Error: Line does not have expected number of fields\n")

if __name__ == "__main__":
    doc_count_mapper()