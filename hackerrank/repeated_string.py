#!/bin/python3

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    x = [0]
    a = 0
    for c in s:
        if c == 'a':
            a += 1
        x.append(a)
    return n//(len(s))*x[-1] + x[n % len(s)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
