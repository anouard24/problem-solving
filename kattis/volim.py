p = int(input())
time = 0
n = int(input())
for _ in range(n):
    t, r = input().split()
    time += int(t)
    if time < 210 and r == "T":
        p = p % 8 + 1
print(p)
