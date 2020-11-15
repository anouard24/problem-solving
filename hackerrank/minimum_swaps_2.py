# https://www.hackerrank.com/challenges/minimum-swaps-2/problem


from mylib.unionfind import UnionFind


def minimumSwaps(arr, n):
    uf = UnionFind()
    for i in range(n):
        if not uf.contains(i):
            uf.add(i)
        v = arr[i] - 1
        if not uf.contains(v):
            uf.add(v)
        uf.unify(i, v)
    return n - uf.components()


if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(minimumSwaps(arr, n))
