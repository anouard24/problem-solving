#!/bin/python3

import os

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    p = 1
    s = 0
    for i in sorted(calorie, reverse=True):
        s += i*p
        p <<= 1
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
