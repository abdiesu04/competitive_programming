class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 , 1 , 1]

        for i in range(n):
            ans = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = ans
        return dp[0]