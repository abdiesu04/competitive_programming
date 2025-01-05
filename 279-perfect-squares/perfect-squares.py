class Solution:
    def numSquares(self, n: int) -> int:
        perfects = []
        for i in range(1,n+1):
            print(i,n)
            if i * i <= n:
                perfects.append(i*i)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for perfect in perfects:
            for i in range(perfect, n+1):
                dp[i] = min(dp[i] , dp[i-perfect] + 1)
        return dp[n]


