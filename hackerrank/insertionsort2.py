n = int(input())
x = list(map(int, str(input()).split()))

for j in range(1, n):
    m = x[j]
    for i in range(j-1, -1, -1):
        if m < x[i]:
            x[i+1] = x[i]
        else:
            x[i+1] = m
            break
    else:
        if x[0] > m:
            x[0] = m
    print(' '.join((str(c) for c in x)))


