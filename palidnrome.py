class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]
        """
        :type s: str
        :rtype: bool
        """
