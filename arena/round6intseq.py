a, p, q = map(int, input().split())

if q == 1:
    print("-1")
elif p % q == 0:
    print("-1")
else:
    c = 0
    u = a
    d = 1
    while True:
        u *= p
        d *= q
        c += 1
        if u % d != 0:
            break
    print(c)
