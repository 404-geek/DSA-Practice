class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)

        col_arr = [-1] * n

        def dfs(node, col):

            val = col_arr[node]

            if  val in (0,1):
                return val == col

            col_arr[node] = col

            for nei in graph[node]:

                if not dfs(nei, col ^ 1):
                    return False

            return True
 

        for node in range(n):
            if col_arr[node] == -1:
                if not dfs(node, 0):
                    return False

        return True        
