class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            counter  = 0
            for i in  range(len(piles)):
                counter += (piles[i] + k - 1) // k
            return counter

        l , r  = 1 , max(piles)
        ans  = -1
        while l <= r:
            mid = l + (r - l) // 2
            print(mid , helper(mid))
            if helper(mid) <= h:
                ans  = mid
                r = mid - 1
            else:
                l  = mid  +1
        return ans

