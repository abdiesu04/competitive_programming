class Solution:
    def longestNiceSubstring(self, s):
        chars = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in chars:
                l1 = self.longestNiceSubstring(s[:i])
                l2 = self.longestNiceSubstring(s[i+1:])
                return max(l1, l2, key=len)
        return s