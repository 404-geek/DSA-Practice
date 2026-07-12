class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        dp = matrix[n-1][:]

        for r in range(n-2, -1, -1):

            temp = [0] * n

            for c in range(n - 1, -1, -1):

                val = matrix[r][c]

                min_dp = float('inf')

                move = [c-1, c, c+1]

                for m in move:

                    if 0 <= m < n:

                        min_dp = min(min_dp, dp[m])

                temp[c] = val + min_dp

            dp = temp

        return min(dp)
                 
            
