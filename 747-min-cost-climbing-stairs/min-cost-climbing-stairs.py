class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dp(num):
            if num in memo:
                return memo[num]
            if num == n - 1 or num == n - 2:
                return cost[num]
            memo[num] = cost[num] + min(dp(num + 1), dp(num + 2))  # Memoize the result
            return memo[num]

        return min(dp(0), dp(1))
