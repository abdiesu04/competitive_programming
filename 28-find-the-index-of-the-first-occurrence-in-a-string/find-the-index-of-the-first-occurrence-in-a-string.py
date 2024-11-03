class Solution:
    def strStr(self, s: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(s)):
            if s[i] == needle[0] and s[i:i+n] == needle:
                return i

        return -1 