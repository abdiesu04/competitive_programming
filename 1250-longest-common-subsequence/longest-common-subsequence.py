class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = {}
        def dp(p1 , p2):
            if p1 == len(t1) or p2 == len(t2):
                return 0
            if (p1,p2) in memo:
                return memo[(p1,p2)]
            if t1[p1] == t2[p2]:
                result  =  1 + dp(p1 + 1, p2 + 1)
            else:
                result = max(dp(p1 + 1, p2), dp(p1, p2 + 1))
            memo[(p1,p2)]  = result
            return result
        return dp(0, 0)