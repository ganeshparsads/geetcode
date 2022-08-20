from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True

        deGree = [0 for i in range(numCourses)]
        adjList = {}

        for edge in prerequisites:
            deGree[edge[0]] += 1

            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[1]].append(edge[0])

        q = deque()
        count = 0

        for idx, i in enumerate(deGree):
            if i == 0:
                count += 1
                q.append(idx)

        while q and count < numCourses:
            curr = q.pop()

            if curr not in adjList:
                continue
            li = adjList[curr]

            for node in li:
                deGree[node] -= 1
                if not deGree[node]:
                    q.append(node)
                    count += 1

                    if count == numCourses:
                        return True

        if count == numCourses:
            return True
        return False

obj = Solution()

n = 6
prerequisites = [[1,0], [2,0], [3,1], [3,2], [4,1], [5,4], [5,2]]
print(obj.canFinish(n, prerequisites))
