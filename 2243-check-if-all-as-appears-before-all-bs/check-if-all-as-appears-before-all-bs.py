class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == 'b' and 'a' in s[i:]:
                return False
        return True
        