class Solution:
    def countGoodStrings(self,low, high, zero, one):
        mod = 10**9 + 7
        dp = [1] + [0] * high
        for i in range(1, high+1):
            dp[i] = (dp[i-zero] + dp[i-one]) % mod
        return sum(dp[low:high+1]) % mod