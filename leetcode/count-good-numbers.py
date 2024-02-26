class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(b,p, mod):
            if p == 0:
                return 1
            if p == 1:
                return b
            y = power(b,p//2, mod)
            return y * y % mod if p % 2 == 0 else y * y * b % mod
            
        return power(5, math.ceil(n/2), (10**9 + 7)) * power(4, n//2, (10**9 + 7)) % (10**9 + 7)
            