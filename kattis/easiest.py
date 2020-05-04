def sumdigits(x):
	s = 0
	while x > 0:
		s += x % 10
		x //= 10
	return s

while True:
	n = int(input())
	if n == 0:
		break

	s = sumdigits(n)
	j = 11
	while sumdigits(n*j) != s:
		j += 1

	print(j)
