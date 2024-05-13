# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]  
        
        def dp(i, prev):
            if i == n:
                return 0
            
            if memo[i][prev] != -1:
                return memo[i][prev]
            
            if prev == -1 or nums[i] > nums[prev]:
                inc = 1 + dp(i + 1, i)
                exc = dp(i + 1, prev)
                memo[i][prev] = max(inc, exc)
            else:
                memo[i][prev] = dp(i + 1, prev)
            
            return memo[i][prev]
        
        return dp(0, -1)


