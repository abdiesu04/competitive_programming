from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurrence = {}  # Dictionary to store the last occurrence index of each character
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in last_occurrence and last_occurrence[s[r]] >= l:
                l = last_occurrence[s[r]] + 1
            last_occurrence[s[r]] = r
            res = max(res, r - l + 1)

        return res