import heapq


def cookies(k, arr):
    h = []
    for i in arr:
        heapq.heappush(h, i)
    if h[0] >= k:
        return 0
    elif len(h) < 2:
        return -1
    j = 0
    while len(h) >= 2 and h[0] < k:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        new = a + 2 * b
        j += 1
        heapq.heappush(h, new)
    return -1 if h[0] < k else j


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)
