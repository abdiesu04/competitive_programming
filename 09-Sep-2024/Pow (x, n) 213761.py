# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        sign = True
        if  n < 0:
            n = -n
            sign = False
        def pow(n):
            if n  == 1:
                return x
            half = pow(n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half
            
        res = pow(n)
        if not sign :
            res = 1 / res
        return res
            