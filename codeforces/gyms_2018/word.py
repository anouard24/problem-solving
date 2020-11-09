# problem name: Word
# date:         10/11/2018

ins = str(input())
up = 0
low = 0
for i, s in enumerate(ins):
    if s.isupper():
        up += 1
    else:
        low += 1

if up > low:
    ins = ins.upper()
else:
    ins = ins.lower()

print(ins)
