class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i : [] for i in range(numCourses)}

        for a,b in prerequisites:
            adj[b].append(a)

        print(adj)

        vis = {i: 0 for i in range(numCourses)}

        def dfs(node):
            
            if vis[node] == 1:
                return False

            if vis[node] == 2:
                return True

            vis[node] = 1

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            vis[node] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        