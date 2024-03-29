class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True for _ in range(n+1)]
        isPrime[0] = False
        isPrime[1] = False

        i = 2
        while i * i <= n:
            if isPrime[i]:
                j = i * i
                while j <= n:
                    isPrime[j] = False
                    j += i
            i += 1
        # print(isPrime)
        cnt = 0
        for i in range(len(isPrime) -1):
            if isPrime[i]:
                cnt += 1
        return cnt