# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(idx, sm):
            if sm == amount:
                return 1
            if sm > amount or idx >= len(coins):
                return 0
            if (idx, sm) not in memo:
                memo[(idx, sm)] = dp(idx, sm + coins[idx]) + dp(idx + 1, sm)
            
            return memo[(idx, sm)]
        
        return dp(0, 0)