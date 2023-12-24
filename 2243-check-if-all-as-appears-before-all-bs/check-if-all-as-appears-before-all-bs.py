class Solution:
    def checkString(self, s: str) -> bool:
        # for i in range(len(s)):
        #     if s[i] == 'b' and 'a' in s[i:]:
        #         return False
        # return True
        if set(s) == {'a'}:
            return True
        i = 0
        while i < len(s) and s[i] == 'a':
            i += 1
        if len(set(s[i:])) == 1:
            return True
        return False


