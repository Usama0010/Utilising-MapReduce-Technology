#!/usr/bin/env python

import sys

def article_data_reducer():
    for line in sys.stdin:
        article_id, section_text = line.strip().split('\t')
        print(f"{article_id}\t{section_text}")

if __name__ == "__main__":
    article_data_reducer()

