from collections import defaultdict
from collections import deque


# def getRatio(start, end, data):
#     dict = defaultdict(list)
    # for node in data:
    #     dict[node[0]].append([node[1], node[2]])
    #     dict[node[1]].append([node[0], 1.0 / node[2]])
#     queue = deque()
#     queue.append((start, 1.0))
#     visited = set()
#     while queue:
#         curr, num = queue.popleft()
#         if curr in visited:
#             continue
#         visited.add(curr)
#         if curr in dict:
#             values = dict.get(curr)
#             next = {}
#             for val in values:
#                 next[val[0]] = val[1]
#             for key in next:
#                 if key not in visited:
#                     if key == end:
#                         return num * next[key]
#                     queue.append((key, num * next[key]))
#     return -1

def currency_conversion(rates, query):
    graph = defaultdict(list)
    for from_curr, to_curr, rate in rates:
        graph[from_curr].append([to_curr, rate])
        graph[to_curr].append([from_curr, 1/rate])

    print(graph)

    start, finish = query
    stack = [[start, 1.0]]
    visited = set()
    while stack:
        node, cur_rate = stack.pop()
        if node in visited or node not in graph:
            continue
        if node == finish:
            return cur_rate
        visited.add(node)
        for child_node, child_rate in graph[node]:
            if child_node not in visited:
                if child_node == finish:
                    return cur_rate*child_rate
                stack.append([child_node, cur_rate*child_rate])
    return -1

data = [("USD", "CAD", 1.3), ("USD", "GBP", 0.71), ("USD", "JPY", 109), ("GBP", "JPY", 155)]
# print(getRatio("GBP", "AUD", data))
print(currency_conversion(data, ("USD", "JPY")))
