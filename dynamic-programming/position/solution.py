class Solution:
	def postion(self, a, b, c, d):
		stack = []

		stack.append((a, b))

		while stack:
			(i,j) = stack.pop()

			if i == c and j == d:
				return True

			if i <= c and (i+j) <= d:
				stack.append((i, i+j))

			if (i + j) <= c and j <= d:
				stack.append((i+j, j))

		return False

obj = Solution()

print(obj.postion(1, 4, 5, 9))
