x, a, b = map(int, input().strip().split())

digits = set(input().strip())
nd = len(digits)

k = 0
for i in range(a, 1 + b):
    if i % x == 0:
        k = i
        break

somme = 0
for j in range(k, 1 + b, x):
    if len(digits | set(str(j))) <= nd:
        somme += 1

print(somme)
