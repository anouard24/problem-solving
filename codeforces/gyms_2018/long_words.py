# problem name: Way Too Long Words
# date:         10/11/2018

n = int(input())

a = []
for i in range(n):
    ins = str(input())
    if len(ins) > 10:
        a.append(ins[0] + str(len(ins) - 2) + ins[-1])
    else:
        a.append(ins)

for i in a:
    print(i)
