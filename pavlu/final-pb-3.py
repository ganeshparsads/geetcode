
arr = [1, 2, 3, 8, 10, 12, 15, 17, 18, 20, 25]

n = len(arr)

j = n//2
i = j - 1

target = 5

min_diff = 100000 # infinity

pair = (0, n-1)

while i >= 0 and j < n:
	if min_diff > abs(arr[i] + arr[j] - target):
		min_diff = arr[i] + arr[j] - target
		pair = (i, j)

	if (arr[i] + arr[j] - target) > 0:
		i -= 1
	else:
		j += 1

print(pair)
print(min_diff)
