
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        odds = 0
        for val in counter.values():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odds = 1
        
        res += odds
        return res