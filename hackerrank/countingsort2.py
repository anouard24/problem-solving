#!/bin/python3

import os

# Complete the countingSort function below.
def countingSort(arr):
    tab = [0]*100
    for i in arr:
        tab[i] += 1
    asr = []
    for i in range(100):
        asr.extend([i]*tab[i])
    return asr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
