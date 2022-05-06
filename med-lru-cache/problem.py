from solution import LRUCache

# Your LRUCache object will be instantiated and called as such:

ip = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

cap = ip.pop(0)

obj = LRUCache(cap[0])

for each in ip:
	if len(each) == 2:
		obj.put(each[0], each[1])
	else:
		print("Data: ", obj.get(each[0]))

