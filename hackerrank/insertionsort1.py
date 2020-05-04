n = int(input())
x = list(map(int, str(input()).split()))

m = x[-1]

for i in range(n-2, -1, -1):
    if m < x[i]:
        x[i+1] = x[i]
        print(' '.join((str(c) for c in x)))
    else:
        x[i+1] = m
        print(' '.join((str(c) for c in x)))
        break
else:
    if x[0] > m:
        x[0] = m
        print(' '.join((str(c) for c in x)))
