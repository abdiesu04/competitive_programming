# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, trans, hold):
            if idx >= len(prices) or trans <= 0:
                return 0

            if (idx, trans, hold) in memo:
                return memo[(idx, trans, hold)]

            if hold:
                sell = prices[idx] + dp(idx + 1, trans - 1, False)
                skip = dp(idx + 1, trans, True)
                memo[(idx, trans, hold)] = max(sell, skip)
            else:
                buy = -prices[idx] + dp(idx + 1, trans, True)
                skip = dp(idx + 1, trans, False)
                memo[(idx, trans, hold)] = max(buy, skip)

            return memo[(idx, trans, hold)]

        return dp(0, 2, False)