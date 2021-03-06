class UnionFind:
    def __init__(self):
        self.size = 0
        self.numComponents = 0
        self.szs = {}
        self.ids = {}

    def add(self, p):
        self.size += 1
        self.numComponents += 1
        self.szs[p] = 1
        self.ids[p] = p

    def contains(self, p):
        return bool(self.ids.get(p))

    def find(self, p):
        r = p
        while r != self.ids[r]:
            r = self.ids[r]
        while p != r:
            pp = self.ids[p]
            self.ids[p] = r
            p = pp
        return r

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentsSize(self, p):
        return self.szs[self.find(p)]

    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return
        if self.szs[root1] < self.szs[root2]:
            self.szs[root2] = self.szs[root2] + self.szs[root1]
            self.ids[root1] = root2
        else:
            self.szs[root1] = self.szs[root1] + self.szs[root2]
            self.ids[root2] = root1
        self.numComponents -= 1


# main program
while True:
    n = int(input())
    if n == -1:
        break

    uf = UnionFind()
    matrix = []
    for v in range(n):
        line = list(map(int, input().split()))
        matrix.append(line)
        uf.add(v)

    for i in range(n):
        f = []
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                f.append(j)
        for k in f:
            for l in f:
                if k != l and matrix[k][l] == 1:
                    uf.unify(i, k)
                    uf.unify(i, l)

    for i in range(n):
        if uf.componentsSize(i) == 1:
            print(i, end=" ")
