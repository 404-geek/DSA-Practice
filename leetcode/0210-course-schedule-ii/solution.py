class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(numCourses)]
        
        for a,b in prerequisites:
            
            adj[a].append(b)

        res = []
        vis = [0] * numCourses

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

            res.append(node)

            return True

        for i in range(numCourses):
            if vis[i] == 0 and not dfs(i):
                return []

        return res

        

            
