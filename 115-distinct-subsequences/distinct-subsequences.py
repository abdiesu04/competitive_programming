class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == t[j]:
                memo[(i,j)] = dp(i+1,j+1) + dp(i+1,j)
            else:
                memo[(i,j)] = dp(i+1,j)
            return memo[(i,j)]
        return dp(0,0)


                