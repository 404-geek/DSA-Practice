class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)

        @cache
        def dfs(row, i):

            if row >= n or i >= len(triangle[row]):
                return 0

            down = dfs(row + 1, i)
            diag = dfs(row + 1, i+1)

            min_sum = triangle[row][i] + min(down, diag)

            return min_sum

        return dfs(0,0)
        
