class Solution:
    def maxScore(self, s: str) -> int:
        total = sum(list(map(int , s)))
        res = 0
        zeros = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
                res = max(res , zeros + total)
            else:
                total -= 1
                res = max(res , zeros + total)
        return res
