class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        vis = set()
        cnt = 0

        def dfs(r,c):

            if grid[r][c] == "#":
                return

            grid[r][c] = "#"

            moves = [[0,-1], [0,1], [1,0], [-1,0]]

            for a,b in moves:
                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr,nc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    cnt+=1

        return cnt

