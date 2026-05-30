from functools import lru_cache

class Solution:
    def frogJump(self, heights, k):

        n = len(heights) - 1

        @lru_cache(None)
        def do_jumps(n):

            if n == 0:
                return 0

            mint = float("inf")

            for j in range(1, k+1):

                if n - j >= 0:

                    v = do_jumps(n-j) + abs(heights[n-j] - heights[n])

                    mint = min(mint, v)

            return mint

        return do_jumps(n)