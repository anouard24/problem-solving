# problem name: Bit++
# date:         15/01/2018

ins = str(input())
n = int(ins)
op = []
for i in range(0, n):
    op.append(str(input()))
x = 0
for i in range(0, n):
    if "--" in op[i]:
        x = x - 1
    if "++" in op[i]:
        x = x + 1
print(x)
