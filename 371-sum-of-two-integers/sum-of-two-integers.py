class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b & mask != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry

        if b > 0:
            return a

        if a >= 2**31:
            return ~(a ^ mask)

        return a