#!/usr/bin/env python

import sys
import math

def indexer_reducer():
    current_word = None
    doc_word_count = {}
    for line in sys.stdin:
        word, doc_tf = line.strip().split('\t')
        doc_id, tf = doc_tf.split(',')
        tf = float(tf)
        if current_word == word:
            doc_word_count[doc_id] = tf
        else:
            if current_word:
                idf = math.log10(1 / len(doc_word_count))
                for doc, tf in doc_word_count.items():
                    tfidf = tf * idf
                    print(f"{doc}\t{current_word},{tfidf}")
                doc_word_count = {}
            current_word = word
            doc_word_count[doc_id] = tf
    if current_word:
        idf = math.log10(1 / len(doc_word_count))
        for doc, tf in doc_word_count.items():
            tfidf = tf * idf
            print(f"{doc}\t{current_word},{tfidf}")

if __name__ == "__main__":
    indexer_reducer()
