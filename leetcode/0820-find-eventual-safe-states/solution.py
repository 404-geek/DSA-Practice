class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)

        state = [0] * n

        res = []

        def dfs(node):

            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        res = []

        for node in range(n):
            if state[node] == 2 or dfs(node):
                res.append(node)

        return res


