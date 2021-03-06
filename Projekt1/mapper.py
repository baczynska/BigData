#!/usr/bin/env python

import sys

def main(separator='\t'):
    for idx, line in enumerate(sys.stdin):
        if idx != 0:
            words = line.split('\t')
            if len(words) < 6:
                continue
            director = 1 if 'director' in words[3] else 0
            actor = 1 if ('actor' in words[3]) or ('actress' in words[3]) or ('self' in words[3]) else 0
            if director or actor:
                print( words[2], director, actor )




if __name__ == "__main__":
    main()