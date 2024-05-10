# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(idx, sell, isCoolDown):
            if idx >= len(prices):
                return 0

            if (idx, sell, isCoolDown) in memo:
                return memo[(idx, sell, isCoolDown)]

            if sell:
                mx = max(prices[idx]  + dp(idx + 2, False, False), dp(idx + 1, True, True))
            elif not sell and isCoolDown:
                mx = dp(idx + 1, sell, False)
            else:
                mx = max(-prices[idx] + dp(idx + 1, True, False), dp(idx + 1, False, False))

            memo[(idx, sell, isCoolDown)] = mx
            return mx

        return dp(0, False, False)