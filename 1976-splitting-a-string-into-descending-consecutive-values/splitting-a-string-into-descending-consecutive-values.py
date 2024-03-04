class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(idx, prev):
            if idx == len(s):
                return True
            for i in range(idx, len(s)):
                val = int(s[idx:i + 1])
                if prev - 1 == val and backtrack(i + 1, val):
                    return True
            return False

        for i in range(len(s)-1):
            start = s[:i+1]
            if backtrack(i+1, int(start)):
                return True
        return False