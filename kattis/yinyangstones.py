s = input()
i = 0
for c in s:
	if c == "B":
		i += 1
	else:
		i -= 1

if i == 0:
	print(1)
else:
	print(0)
