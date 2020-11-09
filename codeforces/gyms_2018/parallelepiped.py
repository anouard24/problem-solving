# problem name: Parallelepiped
# date:         10/11/2018


ins = str(input())

s = list(map(int, ins.split()))

a = (s[0] * s[1] / s[2]) ** 0.5
b = (s[0] * s[2] / s[1]) ** 0.5
c = (s[1] * s[2] / s[0]) ** 0.5

print(int((a + b + c) * 4))
