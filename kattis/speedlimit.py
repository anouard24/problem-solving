while True:
    n = int(input())
    if n == -1:
        break
    last = 0
    miles = 0
    for _ in range(n):
        s, t = map(int, str(input()).split())
        miles += s * (t - last)
        last = t
    print(miles, "miles")
