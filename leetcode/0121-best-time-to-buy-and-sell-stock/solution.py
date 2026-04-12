class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = prices[0]
        ans = 0

        for r in prices:

            if r < l:
                l = r
            else:
                ans = max(ans, r - l)

        return ans










        
        
