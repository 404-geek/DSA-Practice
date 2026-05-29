class Solution:
    @cache
    def fib(self, n: int) -> int:

        if n == 1:
            return 1

        prev1 = 0
        prev2 = 1

        ans = 0

        for i in range(1, n):

            ans = prev2 + prev1
            prev1 = prev2
            prev2 = ans

        return ans


