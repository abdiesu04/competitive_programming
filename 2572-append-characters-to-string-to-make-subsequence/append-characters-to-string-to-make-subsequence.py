class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for char in s:
            if p < len(t) and char == t[p]:
                p += 1
        return len(t) - p