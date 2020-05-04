
from math import sqrt
from itertools import count

def primes():
    yield 2
    for n in count(3, 2):
        for i in range(3, int(sqrt(n))+1, 2):
            if n % i == 0:
                break
        else:
            yield n


q = int(input())

for _ in range(q):
    n = int(input())
    k = 0
    p = 1
    for i in primes():
        v = p * i
        if v <= n:
            p = v
            k += 1
        else:
            break
    print(k)
