from solution import StockSpanner


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()

input1 = [100,80,60,70,60,75,85]

input2 = [100, 80, 110, 90, 60, 70, 95]

for num in input2:
	print(num, obj.next(num))
