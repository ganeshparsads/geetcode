from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct in-degree and adjList
        
        inDegree = [0 for i in range(numCourses)]
        
        adjList = {}
        
        for i in prerequisites:
            inDegree[i[0]] += 1
            if i[1] not in adjList:
                adjList[i[1]] = []
            adjList[i[1]].append(i[0])
        q = deque()
        result = []
        count = 0
        # go through each node
        for idx, i in enumerate(inDegree):
            if i == 0:
                result.append(idx)
                q.append(idx)
                count += 1
        
        while q and count < numCourses:
            curr = q.pop()
            
            if curr not in adjList:
                continue

            li = adjList[curr]
            
            for node in li:
                inDegree[node] -= 1
                if not inDegree[node]:
                    result.append(node)
                    q.append(node)
                    count += 1
                    
                    if count == numCourses:
                        return result
            
        if count == numCourses:
            return result
        else:
            return []
        
                