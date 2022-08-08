class Solution():
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph)-1
        source = 0
        stack = [(source, [source])]
        results = []; path=[source]
        while stack:
            node, path = stack.pop()
            if node == target:
                results.append(path[:])
            for nbr in graph[node]:
                stack.append((nbr, path+[nbr]))
        return results

obj = Solution()
print(obj.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
