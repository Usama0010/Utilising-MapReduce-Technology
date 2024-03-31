#!/usr/bin/env python

import sys

def doc_count_reducer():
    current_word = None
    doc_count = set()
    for line in sys.stdin:
        word, article_id = line.strip().split('\t')
        if current_word == word:
            doc_count.add(article_id)
        else:
            if current_word:
                print(f"{current_word}\t{len(doc_count)}")
            current_word = word
            doc_count = {article_id}
    if current_word:
        print(f"{current_word}\t{len(doc_count)}")

if __name__ == "__main__":
    doc_count_reducer()