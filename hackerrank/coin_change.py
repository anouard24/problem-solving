
# https://www.hackerrank.com/challenges/coin-change/problem


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

    n, m = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units 
    # using coins having the values given by 'c'
    print(getWays(n, c))

