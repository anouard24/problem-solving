# problem name: Beautiful Matrix
# date:         10/11/2018


a = []
for i in range(5):
    ins = str(input())
    a.append(list(map(int, ins.split())))

for i, s in enumerate(a):
    if sum(s) == 1:
        x = s.index(1)
        y = a.index(s)

print(abs(2 - y) + abs(2 - x))
