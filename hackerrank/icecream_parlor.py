from bisect import bisect_left


def BinarySearch(a, x, lo=0): 
    i = bisect_left(a, x, lo=lo) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1


def icecreamParlor(m, arr, n):
    sarr = sorted(arr)
    a = b = -1
    for i in range(n):
        j = BinarySearch(sarr, m-sarr[i], lo=i+1)
        if j != -1:
            a = sarr[i]
            b = m-a
            print(">>",a,b,m)

    i = j = -1
    for k in range(n):
        if arr[k] == b:
            j = k + 1
        if i > 0 and j > 0 and i != j:
            break
        if arr[k] == a:
            i = k + 1
    return sorted([i, j])

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr, n)

        print(*result)
