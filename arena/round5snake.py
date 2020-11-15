t = int(input())

while t > 0:
    x, y = map(int, str(input()).split())
    n3 = 2 * y - x
    if n3 < 0 or n3 % 3 != 0:
        print("NO")
    else:
        n = n3 / 3
        m = y - 2 * n
        if m < 0:
            print("NO")
        else:
            print("YES")
            print(int(m) + int(n))
    t -= 1
