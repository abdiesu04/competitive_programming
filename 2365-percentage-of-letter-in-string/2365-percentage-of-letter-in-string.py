class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        return round(math.floor((s.count(letter)/len(s))*100))