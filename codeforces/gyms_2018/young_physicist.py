# problem name: Young Physicist
# date:         16/01/2018

ins = str(input())
n = int(ins)
op = []
for i in range(0, n):
    op.append(str(input()))
x = 0
y = 0
z = 0
xyz = ""
for s in op:
    x += int(s.split(" ")[0])
    y += int(s.split(" ")[1])
    z += int(s.split(" ")[2])
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
