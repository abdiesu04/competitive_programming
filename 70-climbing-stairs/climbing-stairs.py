class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n  # Initialize the dp array with n elements
        dp[n-1] = 1  # There's only 1 way to climb the last step
        dp[n-2] = 1  # There's only 1 way to climb if you're 2 steps away from the top
        
        for i in range(n-3, -1, -1):  # Iterate backwards from n-3 to 0
            dp[i] = dp[i+1] + dp[i+2]  # Sum the ways from the next two steps
        print(dp)
        return dp[0] + dp[1]
