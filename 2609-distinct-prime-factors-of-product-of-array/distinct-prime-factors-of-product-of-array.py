class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        cnt = 0
        product = 1
        for i in nums:
            product *= i
        
        d = 2
        
        while d * d <= product:
            if (product % d == 0):
                cnt += 1
            while (product % d == 0):
                product //= d
            d += 1
        if product > 1:
            cnt += 1
        print(cnt)
        return cnt