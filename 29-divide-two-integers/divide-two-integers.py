class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31 - 1
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        neg = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            res += multiple
        
        if neg:
            res = -res
        
        return min(max(-2**31, res), 2**31 - 1)

