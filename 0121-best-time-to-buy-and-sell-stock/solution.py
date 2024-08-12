class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        current_max, max_profit = 0, 0
        i = len(prices) -1
        while i >= 0:
            price = prices[i]
            current_max = max(current_max, price)
            potential_profit = current_max - price
            max_profit = max(max_profit, potential_profit)
            i-=1
        return max_profit

            
