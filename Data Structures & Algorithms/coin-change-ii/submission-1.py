from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cnt = 0

        @cache
        def dfs(rem, i):

            nonlocal cnt

            if rem == 0:
                return 1

            if rem < 0 or i == len(coins):
                return 0

            take = dfs(rem - coins[i], i)
            not_take = dfs(rem, i+1)

            return take + not_take
        
        return dfs(amount, 0)
            