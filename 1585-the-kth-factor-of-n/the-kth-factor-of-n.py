class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = 1

        for i in range(1, n + 1):
            if n % i == 0:
                factor = i
                k -= 1
            if factor == n and k > 0:
                return -1
            if k == 0:
                return factor

        return factor

        