
from collections import defaultdict

def equalizeArray(arr):
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    return n - d[max(d, key=d.get)]


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(equalizeArray(arr))
