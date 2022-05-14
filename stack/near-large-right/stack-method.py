def nearest_largest_ele(arr):
	stack = []
	g_map = {}

	for num in reversed(arr):
		if not stack:
			stack.append(num)
			g_map[num] = -1
			continue

		if stack[-1] > num:
			g_map[num] = stack[-1]
			stack.append(num)

		else:
			while stack and stack[-1] <= num:
				print(stack.pop())

			if not stack:
				g_map[num] = -1
			else:
				g_map[num] = stack[-1]
				stack.append(num)

	print(g_map)


arr = [1, 3, 2, 4]
nearest_largest_ele(arr)
