class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(num):
            if num == n:
                return 1
            if num > n:
                return 0
            if num not in memo:
                memo[num] = dp(num + 1) + dp(num + 2)
            return memo[num]
        return dp(0)

            