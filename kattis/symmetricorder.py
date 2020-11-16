k = 1
while True:
    n = int(input())
    if n == 0:
        break

    names = []
    for _ in range(n):
        names.append(str(input()))

    print("SET", k)
    k += 1
    for i in range(0, n, 2):
        print(names[i])
    for i in range(n - 1 - n % 2, 0, -2):
        print(names[i])
