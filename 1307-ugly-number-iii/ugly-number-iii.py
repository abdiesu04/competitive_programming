class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def helper(num):
            ab_lcm = lcm(a, b)
            ac_lcm = lcm(a, c)
            bc_lcm = lcm(b, c)
            abc_lcm = lcm(lcm(a, b), c)

            return (num // a + num // b + num // c) - (num // ab_lcm + num // bc_lcm + num // ac_lcm) + (num // abc_lcm)

        def lcm(x, y):
            return abs(x * y) // gcd(x, y)

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        left, right = 1, 2 * 10 ** 9

        while left < right:
            mid = left + (right - left) // 2
            if helper(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left