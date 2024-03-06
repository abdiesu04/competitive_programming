class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        while l < r:
            mid = l + (r - l) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                r = mid
            else:
                l = mid + 1
        return l