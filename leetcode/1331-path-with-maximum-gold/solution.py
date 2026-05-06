class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        maxi = 0

        def start_traverse(r,c, coll):

            g = grid[r][c]

            coll += g

            grid[r][c] = "#"

            best = 0

            move = [(-1,0), (0,1), (1,0), (0, -1)]

            for a, b in move:

                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and grid[nr][nc] != "#":
                    best = max(best, start_traverse(nr, nc, coll))
    
            grid[r][c] = g
            return g + best

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    maxi = max(maxi, start_traverse(r,c,0))

        return maxi
        
