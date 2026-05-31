class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * (n)
        dp[0] = 1

        for r in range(0, m):
            for c in range(0, n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] = dp[c] + dp[c-1]

        return dp[n-1]
