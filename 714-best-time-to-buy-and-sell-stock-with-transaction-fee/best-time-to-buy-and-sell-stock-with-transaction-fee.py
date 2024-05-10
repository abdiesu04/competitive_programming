class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dp(idx, sell):
            if idx >= len(prices):
                return 0
            
            if (idx, sell) in memo:
                return memo[(idx, sell)]
            
            if sell:
                mx = max(prices[idx] - fee + dp(idx + 1, False), dp(idx + 1, True))
            else:
                mx = max(-prices[idx] + dp(idx + 1, True), dp(idx + 1, False))
            
            memo[(idx, sell)] = mx
            return mx
        
        return dp(0, False)