class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
        res = []
        for i in range(2 , n//2 + 1):
            if is_prime[i]:
                if is_prime[n-i]:
                    res.append([i , n - i])
        return res
