# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def maxProfit(idx, sell):
            if idx >= len(prices):
                return 0
            
            if (idx, sell) in memo:
                return memo[(idx, sell)]
            
            if sell:
                mx = max(prices[idx] - fee + maxProfit(idx + 1, False), maxProfit(idx + 1, True))
            else:
                mx = max(-prices[idx] + maxProfit(idx + 1, True), maxProfit(idx + 1, False))
            
            memo[(idx, sell)] = mx
            return mx
        
        return maxProfit(0, False)