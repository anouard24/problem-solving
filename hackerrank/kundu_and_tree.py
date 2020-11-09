from mylib.unionfind import UnionFind


def comb(n, k):
    # Remove the next two lines if out-of-range check is not needed
    if k < 0 or k > n:
        return 0
    x = 1
    for i in range(min(k, n - k)):
        x = x*(n - i)//(i + 1)
    return x


if __name__ == "__main__":
    mod = 1000000007
    n = int(input())
    red_uf = UnionFind()
    for i in range(1, n + 1):
        red_uf.add(i)
    for i in range(1, n):
        a, b, c = input().split(" ")
        if c == "b":
            red_uf.unify(int(a), int(b))
    nc = red_uf.components()
    if nc < 3:
        print("0")
    else:
        v = comb(n, 3)
        for i in red_uf.roots():
            n_i = red_uf.componentsSize(i)
            v -= comb(n_i, 3)
            v -= comb(n_i, 2) * (n - n_i)
        print(v % mod)
