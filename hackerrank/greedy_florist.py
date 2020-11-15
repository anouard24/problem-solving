# https://www.hackerrank.com/challenges/greedy-florist/problem


def getMinimumCost(k, c, n):
    c.sort(reverse=True)
    s = i = j = 0
    while i < n:
        if i % k == 0:
            j += 1
        s += c[i] * j
        i += 1
    return s


if __name__ == "__main__":

    n, k = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c, n)
    print(minimumCost)
