class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = deque([source])
        alreadyChecked = set()

        while queue:
            currNode = queue.popleft()

            if currNode == destination:
                return True

            if currNode in alreadyChecked:
                continue
            
            alreadyChecked.add(currNode)

            for nextNode in graph[currNode]:
                queue.append(nextNode)

        return False

