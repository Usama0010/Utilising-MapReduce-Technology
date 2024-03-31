#!/usr/bin/env python

import sys

def query_reducer():
    relevant_docs = {}
    for line in sys.stdin:
        word, doc_id = line.strip().split('\t')
        if doc_id != 'query':
            if doc_id in relevant_docs:
                relevant_docs[doc_id].add(word)
            else:
                relevant_docs[doc_id] = {word}
    for doc_id, words in relevant_docs.items():
        print(f"{doc_id}\t{','.join(words)}")

if __name__ == "__main__":
    query_reducer()

