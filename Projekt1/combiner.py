#!/usr/bin/env python

from operator import itemgetter
import sys
import os

current_nconst = ""
current_dir = []
current_act = []

def print_array_content(arr):
    result = ""
    for x in arr:
        result += (str(x) + " ")
    return  result

# input comes from STDIN
for line in sys.stdin:
    words = line.split(" ")
    nconst = words[0]
    if current_nconst == nconst:
        current_act.append(int(words[2]))
        current_dir.append(int(words[1]))
    else:
        if current_act != []:
            print(f"{current_nconst},{print_array_content(current_dir)},{print_array_content(current_act)}")
        current_dir = []
        current_act = []
        current_nconst = nconst
        current_act.append(int(words[2]))
        current_dir.append(int(words[1]))

# def main_algorith(lines):
#     for line in lines:
#         words = line.split(" ")
#         nconst = words[0]
#         if current_nconst == nconst:
#             current_act.append(int(words[2]))
#             current_dir.append(int(words[1]))
#         else:
#             if current_act != []:
#                 print(f"{current_nconst},{print_array_content(current_dir)},{print_array_content(current_act)}")
#             current_dir = []
#             current_act = []
#             current_nconst = nconst
#             current_act.append(int(words[2]))
#             current_dir.append(int(words[1]))

# def main():
#     sorted_line = sorted(sys.stdin, key=str.split(" ")[0])
#     main_algorith(sorted_line)
#
#
# if __name__ == "__main__":
#     main()
