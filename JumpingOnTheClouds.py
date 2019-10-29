#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0
    jumps = 0
    while current < len(c) - 1:
        if current + 2 < len(c) and c[current + 2] !=1:
            current += 1
        current += 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split(' ')))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
