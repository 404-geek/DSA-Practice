class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r_len = len(grid)
        c_len = len(grid[0])
        island = 0

        visited_set = set()
        
        def dfs(r,c):

            if (r,c) in visited_set:
                return

            visited_set.add((r,c))

            moves = [[1,0] , [-1,0], [0,1], [0,-1]]

            for i, j in moves:

                nr = r + i
                nc = c + j

                if 0 <= nr < r_len and 0 <= nc < c_len and grid[nr][nc] == "1":
                    dfs(nr,nc)


        for r in range(r_len):
            for c in range(c_len):

                if grid[r][c] == "1" and (r,c) not in visited_set:
                    dfs(r,c)
                    island+=1
        
        return island




        
