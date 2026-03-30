class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        curr_low, profit = 101, 0
        for r in range(len(prices)):
            if prices[r] < curr_low:
                curr_low = prices[r]
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
        
        return profit