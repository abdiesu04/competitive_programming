class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
    
        if n % 3 == 0:
            return 3 ** (n // 3)

        if n % 3 == 1:
            return 4 * (3 ** (n // 3 - 1))

        return 2 * (3 ** (n // 3))