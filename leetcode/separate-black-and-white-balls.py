class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt_zero = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                res += cnt_zero
            else:
                cnt_zero += 1
        return res