class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def find(self, x):
        # base case
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        
        if x != y:
            # print(x)
            # print(y)
            if self.ranks[x] > self.ranks[y]:
                self.parents[y] = x

            elif self.ranks[x] < self.ranks[y]:
                self.parents[x] = y
            else:
                self.parents[y] = x
                self.ranks[x] += 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected):
        obj = UnionFind()
        
        size = len(isConnected)

        # import pdb
        # pdb.set_trace()
        
        for i in range(size):
            for j in range(i, size):
                if i not in obj.parents:
                    obj.parents[i] = i
                    obj.ranks[i] = 1
                if j not in obj.parents:
                    obj.parents[j] = j
                    obj.ranks[j] = 1

                if i != j and isConnected[i][j] == 1:
                    obj.union(i, j)
        
        
        hSet = set()
        
        for i in range(size):
            p = obj.find(i)
            print(i, p)
            hSet.add(obj.parents[i])

        return len(hSet)

