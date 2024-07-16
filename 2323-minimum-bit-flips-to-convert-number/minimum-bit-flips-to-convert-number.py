class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        cnt = 0

        for i in range(32):
            if 1 & res >> i:
                cnt += 1
        return cnt