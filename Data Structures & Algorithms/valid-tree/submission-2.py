class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i : [] for i in range(n)}

        for u, v in edges:

            adj[u].append(v)
            adj[v].append(u)

        vis = set()

        def dfs(node, parent):

            if node in vis:
                return False
            
            vis.add(node)

            for nei in adj[node]:

                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(vis) == n
