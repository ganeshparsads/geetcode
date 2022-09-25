
a = [1, 2, 3, 4, 5]

prefix_sum = [0 for i in range(len(a))]

for idx, i in enumerate(a):
	if idx == 0:
		prefix_sum[idx] = i
	else:
		prefix_sum[idx] = prefix_sum[idx-1] + i


# output required is sum of value from index 2 to 4

# l = 2
# r = 4

l = 0
r = 4

if l > 0:
	result = prefix_sum[r] - prefix_sum[l-1]
else:
	result = prefix_sum[r]

print(result)
