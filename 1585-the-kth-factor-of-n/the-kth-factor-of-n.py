class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact_count = 0
        for i in range(1,n+1):
            if (n%i == 0):
                fact_count += 1
                if fact_count == k:
                    return i
        return -1