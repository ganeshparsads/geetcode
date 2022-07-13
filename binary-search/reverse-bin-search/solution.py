# Python3 program to implement
# the above approach

# Function to search if element X
# is present in reverse sorted array
def binarySearch(arr, N, X):
	
	# Store the first index of the
	# subarray in which X lies
	start = 0

	# Store the last index of the
	# subarray in which X lies
	end = N

	while (start <= end):

		# Store the middle index
		# of the subarray
		mid = start + (end - start) // 2

		# Check if value at middle index
		# of the subarray equal to X
		if (X == arr[mid]):

			# Element is found
			return mid

		# If X is smaller than the value
		# at middle index of the subarray
		elif (X < arr[mid]):
			print(X, arr[mid])

			# Search in right
			# half of subarray
			print("Before: ", start)
			start = mid + 1
			print("After: ", start)
			print(arr[start])
		else:
			print(X, arr[mid])

			# Search in left
			# half of subarray
			end = mid - 1

	# If X not found
	return -1

# Driver Code
if __name__ == '__main__':
	
	arr = [ 5, 4, 3, 2, 1 ]
	N = len(arr)
	X = 5
	
	print(binarySearch(arr, N, X))

# This code is contributed by mohit kumar 29
