class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r,c):

            if grid[r][c] == 0:
                return

            lo = 1
            grid[r][c] = 0
            
            moves = [(-1,0), (1,0), (0,1), (0,-1)]

            for a,b in moves:

                nr = a+r
                nc = b+c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    lo += dfs(nr,nc)

            return lo
            
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    a = dfs(r,c)
                    max_area = max(a, max_area)
        
        return max_area



        
