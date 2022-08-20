from copy import deepcopy

ip = [1, -2, 1, 1, 3, 2, 1, -2]

distinct = {}

last_index = {}

n = len(ip)

k = 2

k_map = {}

for i in range(k):
	k_map[i] = 1


for idx, i in range(n-1, -1, -1):
	k_map = {}
	j = idx
	last_index{i} = idx

	if i not in last_index:
		last_index[i] = idx
	else:
		last_index[i] = idx
