class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
        factors.append(n)
        print(factors)
        return factors[k-1] if k -1 < len(factors) else -1
        