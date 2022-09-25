from collections import deque

class Solution:
    def coinChange(self, coins, amount):
        # BFS way
        # Adjacency List
        adjList = {}
        for i in range(amount, -1, -1):
            newList = []
            for j in coins:
                if j <= i:
                    newList.append(i-j)
            adjList[i] = newList
            # print(adjList)
        print(adjList)

        # run bfs
        bfsStack = deque()
        bfsStack.append(amount)
        cnt = 0
        import pdb
        pdb.set_trace()
        while bfsStack:
            size = len(bfsStack)
            for i in range(size):
                curr = bfsStack.popleft()
                if curr == 0:
                    return cnt
                for neigh in adjList[curr]:
                    bfsStack.append(neigh)
            cnt += 1
            print(bfsStack)
        
        return -1


obj = Solution()
print(obj.coinChange([1, 2, 5], 100))
