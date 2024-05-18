# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dp(start):
            if start == len(s):
                return -1 

            minCuts = float('inf')  

            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    cuts = 1 + dp(end)  
                    minCuts = min(minCuts, cuts)
 
            return minCuts

        return dp(0)