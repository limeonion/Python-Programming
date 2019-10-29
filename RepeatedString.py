#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = 0

    l = len(s)
    length = l

    for i in range(length):
        if s[i] == 'a':
            cnt += 1
    
    count_str = n//length 
    count = count_str * cnt
    x = count_str * length

    i = 0
    while x < n:
        if s[i] == 'a':
            count += 1
            x += 1
        else:
            x += 1
        i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
