class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if node in safe:
                return safe[node]

            safe[node] = False
            for i in graph[node]:
                if not dfs(i):
                    return safe[i]
            safe[node] = True
            return safe[node]

        res = []
        safe = {}
        for node in range(len(graph)):
            if dfs(node):
                res.append(node)

        return res