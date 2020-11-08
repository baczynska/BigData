#!/usr/bin/env python

from operator import itemgetter
import sys
import os

current_nconst = ""
current_dir = 0
current_act = 0

# input comes from STDIN
for line in sys.stdin:
    words = line.split(" ")
    nconst = words[0]
    if current_nconst == nconst:
        current_act + int(words[2])
        current_dir += int(words[1])
    else:
        if current_act+current_dir != 0:
            print(current_nconst, current_dir, current_act)
        current_dir = 0
        current_act = 0
        current_nconst = nconst
        current_act += int(words[2])
        current_dir += int(words[1])
