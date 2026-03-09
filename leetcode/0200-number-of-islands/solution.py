class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cols = len(grid[0])
        rows = len(grid)
        islands = 0
        vis = set()

        def dfs(i,j):

            if (i,j) in vis:
                return

            vis.add((i,j))

            move = [(0,1), (1,0), (-1,0), (0,-1)]

            for r,c in move:

                nc = j + c
                nr = i + r

                if  0 <= nc < cols and 0 <= nr < rows and grid[nr][nc] == "1" and (nr,nc) not in vis:

                    dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in vis and grid[i][j] == "1":

                    dfs(i,j)
                    islands+=1

        return islands

            
        
