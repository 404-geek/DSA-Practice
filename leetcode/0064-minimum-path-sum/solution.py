class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        @cache
        def move(r,c):

            if r >= rows or c >= cols:
                return float("inf")

            if r == rows - 1 and c == cols - 1:
                return grid[r][c] 

            return grid[r][c] + min(move(r, c+1), move(r+1, c))

        return move(0,0)
