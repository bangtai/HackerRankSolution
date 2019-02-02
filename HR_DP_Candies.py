#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    ltr = [1] * len(arr)
    rtl = [1] * len(arr)
    candy = []

    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            ltr[i + 1] = ltr[i] + 1

    for j in range(n - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            rtl[j] = rtl[j + 1] + 1

    for k in range(n):
        candy.append(max(ltr[k], rtl[k]))

    return sum(candy)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
