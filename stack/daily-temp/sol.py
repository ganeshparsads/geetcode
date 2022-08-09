from collections import deque

start = 225

required_sum = start//10 + start%10

num = deque(str(start))

while required_sum != 0:

	for i in range(len(num)-1, -1, -1):
		if num[i] != 9:
			num[i] = '9'
			break
		num.appendleft(0)

	curr_sum = 0
	for i in num:
		curr_sum += int(i)

	required_sum = required_sum - curr_sum

	if required_sum > 9:
		continue

	for i in range(len(num)-1, -1, -1):
		

	break
