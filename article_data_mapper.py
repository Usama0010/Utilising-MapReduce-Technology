#!/usr/bin/env python

import sys

def article_data_mapper():
    for line in sys.stdin:
        data = line.strip().split(',')
        if len(data) >= 4:
            article_id, section_text = data[0], data[3]
            print(f"{article_id}\t{section_text}")

if __name__ == "__main__":
    article_data_mapper()

