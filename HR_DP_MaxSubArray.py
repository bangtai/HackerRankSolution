#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    result = 0
    insum = 0
    notinsum = 0
    for num in arr:
        result = max(result, notinsum + num)

        nextinsum = notinsum + num
        nextnotinsum = max(insum, notinsum)

        insum = nextinsum
        notinsum = nextnotinsum

    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
