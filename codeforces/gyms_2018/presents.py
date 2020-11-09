# problem name: Presents
# date:         15/01/2018

ins = str(input())
n = int(ins)
p = [0] * (n + 1)
xy = str(input())
tab = xy.split(" ")
i = 0
for i in range(1, n + 1):
    p[i] = int(tab[i - 1])

friend = [0] * (n + 1)
for i in range(1, n + 1):
    friend[p[i]] = i
strr = ""
for i in range(1, n + 1):
    strr += str(friend[i]) + " "
print(strr)
