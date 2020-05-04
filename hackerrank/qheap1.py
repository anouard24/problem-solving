import heapq

n = int(input())
h = []
for _ in range(n):
    q = input().split()
    if len(q) == 1:
        print(h[0])
    else:
        v = int(q[1])
        if q[0] == "1":
            heapq.heappush(h, v)
        else:
            if h[0] == v:
                heapq.heappop(h)
            elif h[-1] == v:
                h.pop()
            else:
                i = h.index(v)
                h[i] = h[-1]
                h.pop()
                heapq._siftup(h, i)
                heapq._siftdown(h, 0, i)
