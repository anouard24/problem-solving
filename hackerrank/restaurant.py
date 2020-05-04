from math import gcd

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print("1")
    else:
        print((a * b) // pow(gcd(a, b), 2))
