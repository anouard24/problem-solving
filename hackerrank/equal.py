# https://www.hackerrank.com/challenges/equal/problem


def getn(x):
    s = x // 5
    x %= 5
    s += x // 2
    x %= 2
    s += x
    return s


def equal(arr):
    arr.sort()
    s = 0
    for i in arr:
        s += getn(i - arr[0])
    return s


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        print(equal(arr))
