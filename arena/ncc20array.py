from collections import deque
import heapq

n, k = map(int, input().strip().split(" "))

arr = []
for i in range(n):
    xs = map(int, input().strip().split(" "))
    xs = deque(xs)
    m = xs.popleft()
    for j in range(m):
        heapq.heappush(arr, xs[j])

somme = 0
for i in range(k):
    somme += heapq.heappop(arr)

print(somme)
