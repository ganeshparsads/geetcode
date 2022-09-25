import heapq

class Employee:
	def __init__(self, n, d, yos, s):
		self.name = n
		self.designation = d
		self.yos = yos
		self.s = s

	def print_me(self):
		print("Name: ", self.name)
		print("Designation: ", self.designation)
		print("Yos: ", self.yos)
		print("Salary: ", self.s)

	def __lt__(self, next):
		# for minHeap return true if self < next
		# for maxHeap return true if self > next

		print(self.yos, next.yos)
		return self.yos > next.yos

# creating objects
e1 = Employee('Anish', 'manager', 3, 24000)
e2 = Employee('kathy', 'programmer', 2, 15000)
e3 = Employee('Rina', 'Analyst', 5, 30000)
e4 = Employee('Vinay', 'programmer', 1, 10000)

minHeap = []

heapq.heappush(minHeap, e1)
# import pdb
# pdb.set_trace()
heapq.heappush(minHeap, e2)
heapq.heappush(minHeap, e3)
heapq.heappush(minHeap, e4)


for i in range(0, len(minHeap)):
    minHeap[i].print_me()
    print()

length = len(minHeap)

for i in range(0, length):
	heapq.heappop(minHeap).print_me()