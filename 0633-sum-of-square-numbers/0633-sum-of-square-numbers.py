class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left , right = 0 , int(c**0.5)
        res = False
        while left <= right :
            s = left**2 + right**2 
            if s == c:
                return True
            elif s < c:
                left += 1
            elif s > c:
                right -= 1
        return res
            
