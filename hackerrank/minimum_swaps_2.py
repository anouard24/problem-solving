#!/bin/python3

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

import os

from mylib.unionfind import UnionFind


def minimumSwaps(arr, n):
    uf = UnionFind()
    for i in range(n):
        if not uf.contains(i):
            uf.add(i)
        v = arr[i]-1
        if not uf.contains(v):
            uf.add(v)
        uf.unify(i, v)
    return n - uf.components()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()
