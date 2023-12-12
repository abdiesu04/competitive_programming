class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
        return res[k-1] if len(res) >= k else -1