n = int(input())
cups = []
for _ in range(n):
    a, b = str(input()).split()
    if a.isdigit():
        cups.append((int(a) // 2, b))
    else:
        cups.append((int(b), a))

cups.sort()

for i, c in cups:
    print(c)
