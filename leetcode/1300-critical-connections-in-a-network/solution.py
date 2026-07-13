class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj = [[] for _ in range(n)]

        for conn in connections:

            src = conn[0]
            dest = conn[1]

            adj[src].append(dest)
            adj[dest].append(src)
        
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []
        timer = [1]

        def dfs(node, parent):
            
            vis[node] = 1
            tin[node] = low[node] = timer[0]
            timer[0]+=1

            for nei in adj[node]:
                if nei == parent: continue

                if vis[nei] == 0:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])

                    if low[nei] > tin[node]:
                        bridges.append((node, nei))
                else:
                    low[node] = min(low[node], low[nei])

        dfs(0, -1)
        
        return bridges



            

        
        
