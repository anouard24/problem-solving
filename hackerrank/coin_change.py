#!/bin/python3

# https://www.hackerrank.com/challenges/coin-change/problem

import os

def getWays(n, c):
    c.sort()
    coins = len(c)+1
    mem = [0]*coins
    for i in range(coins):
        mem[i] = [0]*(n+1)
    
    for i in range(1, coins):
        for j in range(n+1):
            if j < c[i-1]:
                mem[i][j] = mem[i-1][j]
            elif j == c[i-1]:
                mem[i][j] = mem[i-1][j] + 1
            else:
                mem[i][j] = mem[i-1][j] + mem[i][j - c[i-1]]
    return mem[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
