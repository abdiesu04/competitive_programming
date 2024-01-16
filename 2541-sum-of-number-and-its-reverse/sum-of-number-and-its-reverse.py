class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            s = str(i)
            sr = s[::-1]
            if int(s) + int(sr) == num:
                return True
        return False
        