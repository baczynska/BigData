#!/usr/bin/env python

from operator import itemgetter
import sys


# input comes from STDIN
for line in sys.stdin:
    words = line.split(",")
    nconst = words[0]
    arr_dir = words[1].split( )
    arr_act = words[2].split( )
    result_dir = sum([ int(x) for x in arr_dir ])
    result_act = sum([ int(x) for x in arr_act ])
    print(nconst, result_dir, result_act)
