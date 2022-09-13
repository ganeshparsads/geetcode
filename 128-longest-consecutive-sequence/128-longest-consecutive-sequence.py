class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        else:
            x = self.find(self.parents[x])
            return x
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        
        if x != y:
            # merge x to y
            self.parents[y] = x
            self.ranks[x] += self.ranks[y]
        
        return self.ranks[x]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)        
        res = 0
        obj = UnionFind()
        
        for i in nums:
            size = 1
            if i not in obj.parents:
                obj.parents[i] = i
                obj.ranks[i] = 1
                
                if i+1 in obj.parents:
                    size = obj.union(i, i+1)
                if i-1 in obj.parents:
                    size = obj.union(i-1, i)
                
                res = max(res, size)
        
        return res
                
            
        