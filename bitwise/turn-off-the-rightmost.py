def turnOffTheRightmost(x):
	m = 1
	while x & m == 0:
		m = m << 1

	x = x ^ m
	return x

print(turnOffTheRightmost(12))
