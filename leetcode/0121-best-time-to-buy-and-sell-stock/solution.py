class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mi = prices[0]
        prof = 0

        for j in prices:

            if j < mi:
                mi = j


            else:
                prof = max(prof, j - mi)

        return prof
                








        
        
