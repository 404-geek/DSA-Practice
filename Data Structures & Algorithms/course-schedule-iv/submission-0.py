from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj  = [[] for _ in range(numCourses)]

        for preq in prerequisites:
            a, b = preq

            adj[b].append(a)

        @cache
        def dfs(node, target):

            if node == target:
                return True

            for nei in adj[node]:

                if dfs(nei, target):
                    return True

            return False

        res = []

        for q in queries:

            target, node = q

            res.append(dfs(node, target))

        return res

            
        