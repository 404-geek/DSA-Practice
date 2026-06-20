class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        arr = [[] for i in range(n)]

        print(arr)

        for i in range(n):
            for j in range(n):

                if isConnected[i][j] == 1  and j != i:
                        arr[i].append(j)

        vis = [0] * n

        def dfs(i):

            if vis[i] == 1:
                return

            vis[i] = 1

            for nei in arr[i]:
                dfs(nei)

        cnt = 0
        
        for i in range(n):
            if vis[i] == 0:
                cnt+=1
                dfs(i)

        return cnt
        
