class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxProfit = 0

        while(r < len(prices)):
            profit = prices[r] - prices[l]

            if profit < 0:
                l += 1
            else:
                maxProfit = max(profit, maxProfit)
                r += 1
        
        return maxProfit