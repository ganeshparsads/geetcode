# Python3 program for the
# above approach

# Function to return the
# minimum string of length
# d having the sum of digits s
def helper(d, s):

	# Return a string of
	# length d
	ans = ['0'] * d

	for i in range(d - 1,
				-1, -1):

		# Greedily put 9's
		# in the end
		if (s >= 9):
			ans[i] = '9'
			s -= 9

		# Put remaining sum
		else:
			c = chr(s +
					ord('0'))
			ans[i] = c;
			s = 0;

	return ''.join(ans);

# Function to find the
# smallest number greater
# than Y whose sum of
# digits is X
def findMin(x, Y):

	# Convert number y
	# to string
	y = str(Y);
	n = len(y)
	p = [0] * n

	# Maintain prefix sum
	# of digits
	for i in range(n):
		p[i] = (ord(y[i]) -
				ord('0'))
		if (i > 0):
			p[i] += p[i - 1];

	# Iterate over Y from the
	# back where k is current
	# length of suffix
	n - 1
	k = 0
	
	while True:

		# Stores current digit
		d = 0;
		if (i >= 0):
			d = (ord(y[i]) -
				ord('0'))

		# Increase current
		# digit
		for j in range(d + 1,
					10):

			# Sum upto current
			# prefix
			r = ((i > 0) *
				p[i - 1] + j);

			# Return answer if
			# remaining sum can
			# be obtained in suffix
			if (x - r >= 0 and
				x - r <= 9 * k):

				# Find suffix of length
				# k having sum of digits
				# x-r
				suf = helper(k,
							x - r);

				pre = "";
				if (i > 0):
					pre = y[0 : i]

				# Append current
				# character
				cur = chr(j +
						ord('0'))
				pre += cur;

				# Return the result
				return pre + suf;

		i -= 1
		k += 1	

# Driver Code
if __name__ == "__main__":
			
# Given Number and Sum
	x = 36;
	y = 99;

	# Function Call
	print ( findMin(x, y))

# This code is contributed by Chitranayal
