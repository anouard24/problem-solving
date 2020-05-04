cups = [1, 0, 0]
s = str(input())
for c in s:
	if c == 'A':
		cups[0], cups[1] = cups[1], cups[0]
	elif c == 'B':
		cups[2], cups[1] = cups[1], cups[2]
	else:
		cups[0], cups[2] = cups[2], cups[0]
print(cups.index(1)+1)
