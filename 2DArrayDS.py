#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    for index, line1 in enumerate(arr):
        if index + 2 == len(arr):
            break

        line2 = arr[index + 1]
        line3 = arr[index + 2]

        pattern1 = []
        pattern2 = []

        for j, val in enumerate(line1):
            val2 = line2[j]
            val3 = line3[j]

            pattern1.append(val + val3)
            pattern2.append(val + val2 + val3)
            if len(pattern1) >= 3:
                hourglasses.append(pattern1[-1] + pattern2[-2] + pattern1[-3])
    return max(hourglasses)
                                                                                                                                                                                                                                                                                                                 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
