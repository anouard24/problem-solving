n = int(input())

for i in range(1, 1 + n):
    t, s = input().strip().split(" ")
    t = int(t)
    print(i, end=" ")
    for j in range(1, 1 + len(s)):
        if j != t:
            print(s[j - 1], end="")
    print()
