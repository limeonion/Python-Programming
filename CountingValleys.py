#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    alt = 0
    i = 0
    for i in range(n):
        if s[i] == 'U':
            alt += 1
            if alt == 0:
                valley += 1
        else:
            alt -= 1

    return valley



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
