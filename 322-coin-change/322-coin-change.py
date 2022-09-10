from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS way
        # Adjacency List
        adjList = {}
        for i in range(amount, -1, -1):
            newList = []
            for j in coins:
                if j <= i:
                    newList.append(i-j)
            adjList[i] = newList

        # run bfs
        bfsStack = deque()
        bfsStack.append(amount)
        cnt = 0
        visited = set()
        while bfsStack:
            size = len(bfsStack)
            for i in range(size):
                curr = bfsStack.popleft()
                if curr == 0:
                    return cnt
                for neigh in adjList[curr]:
                    if neigh not in visited:
                        bfsStack.append(neigh)
                        visited.add(neigh)
            cnt += 1
        
        return -1
        # dyncamic programming way
#         memo = [amount + 1] * (amount + 1)

#         # base case
#         memo[0] = 0

#         for i in range(1, amount+1):
#                 for c in coins:
#                     if i - c >= 0:
#                         memo[i] = min(memo[i], 1 + memo[i-c])

#         return memo[amount] if memo[amount] != (amount + 1) else -1

