#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, s, d, m):
    sum1 = 0
    count = 0
    for i in range(m):
        sum1 = sum1+s[i]
    if n==m:
        if sum1 == d:
            return 1
    for i in range(n-m+1):
        print("sum1= ",sum1)
        if sum1 == d:
            count = count+1
        sum1 = sum1 - s[i]
        if m+i < n:
            sum1 = sum1 + s[m+i]
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
