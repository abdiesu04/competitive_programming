# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9 ) + 7
        even_cnt  = n // 2 if n % 2 == 0 else n // 2 + 1
        odd_cnt = n // 2

        res = pow(5 , even_cnt , mod) * pow(4 , odd_cnt, mod)
        return res % mod