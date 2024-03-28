class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        return res + startValue - target