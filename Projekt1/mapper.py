#!/usr/bin/env python

import sys

def main(separator='\t'):
    for idx, line in enumerate(sys.stdin):
        if idx != 0:
            words = line.split('\t')
            if len(words) < 6:
                continue
            director = True if 'director' in words[3] else False
            actor = True if ('actor' in words[3]) or ('actress' in words[3]) or ('self' in words[3]) else False
            if director or actor:
                print( words[2], int(director), int(actor) )




if __name__ == "__main__":
    main()