class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        j = 1
        res = 0

        while j < len(prices):

            if prices[i] < prices[j]:

                res = max(prices[j] - prices[i], res)

                j+=1
            
            elif prices[j] <= prices[i]:

                i = j
                j+=1
            
            else:
                i+=1
                j+=1

        return res




        
