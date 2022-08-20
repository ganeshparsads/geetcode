from collections import deque

class Solution:
    def getZeroDegreeIdx(self, deGree):
        n = len(deGree)
        for i in range(n-1, -1, -1):
            if deGree[i] == 0:
                return i
        return n-1

    def countValidNodes(self, deGree):
        count = 0
        for i in deGree:
            if i != -1:
                count += 1
        return count

    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        adjList = {}
        deGree = [-1 for i in range(numCourses)]
        dfsStack = deque()
        validNodes_count = 0

        # create adjList and inDeGree array
        for node in prerequisites:
            if node[1] not in adjList:
                adjList[node[1]] = []
            adjList[node[1]].append(node[0])

            if deGree[node[0]] == -1:
                validNodes_count += 1
                deGree[node[0]] = 0
            if deGree[node[1]] == -1:
                validNodes_count += 1
                deGree[node[1]] = 0
            
            if node[1] != node[0]:
                deGree[node[0]] += 1
        
        count = 0

        # add zeroth indexed values to stack
        for idx, val in enumerate(deGree):
            if val == 0:
                count += 1
                dfsStack.append(idx)
        
        print(deGree)
        print(adjList)

        # validNodes_count = self.countValidNodes(deGree)

        # root = self.getZeroDegreeIdx(deGree)
        # dfsStack.append(root)
        # import pdb
        # pdb.set_trace()
        
        while dfsStack:
            curr = dfsStack.popleft()
            if curr not in adjList:
                continue
            # curr adjacent nodes
            for node in adjList[curr]:
                # reduce degree
                deGree[node] -= 1
                
                if not deGree[node]:
                    dfsStack.append(node)
                    count += 1
        
        print(validNodes_count)
        print(count)

        if validNodes_count == count:
            return True
        else:
            return False

obj = Solution()

n = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
print(obj.canFinish(n, prerequisites))
