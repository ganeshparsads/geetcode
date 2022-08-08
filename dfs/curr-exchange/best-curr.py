class Solution:
    def __init__(self):
        self.graph = {}

    def get_currency_exchange_rate(self, source, target):

        def backtrack(current, seen):
            if current == target:
                return 1

            product = -1
            if current in self.graph:
                for neighbor in self.graph[current]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        product = max(product, self.graph[current][neighbor] * backtrack(neighbor, seen))
                        seen.remove(neighbor)

            if product < 0:
                return -1
            else:
                return product

        return backtrack(source, {source})

    def create_graph(self, ip):
        for node in ip.split(';'):
            curr = node.split(',')

            if curr[0] not in self.graph:
                self.graph[curr[0]] = {}
            self.graph[curr[0]][curr[1]] = float(curr[2])

        print(self.graph)

ip = "USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155"

ip2 = "USD,GBP,0.7;USD,JPY,109;GBP,JPY,155;CAD,CNY,5.27;CAD,KRW,921"

obj = Solution()
curr1 = "USD"
curr2 = "JPY"
obj.create_graph(ip)
print(obj.get_currency_exchange_rate(curr1, curr2))

curr1 = "USD"
curr2 = "CNY"
obj2 = Solution()
obj2.create_graph(ip2)
print(obj2.get_currency_exchange_rate(curr1, curr2))

# {'USD': {'JPY': '109', 'GBP': '0.71', 'CAD': '1.3'}, 'GBP': {'JPY': '155'}}
# g = {
#     "USD": {"CAD": 1.3, "GBP": 0.71, "JPY": 109},
#     "GBP": {"JPY": 155}
# }

# print(get_currency_exchange_rate(curr1, curr2, g))

# ("USD", "CAD", 1.3), ("USD", "GBP", 0.71), ("USD", "JPY", 109), ("GBP", "JPY", 155)