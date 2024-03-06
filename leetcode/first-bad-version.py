# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # nums = [i for i in range(1, n)]
        l , r = 0 , n -1
        while l <= r:
            mid = l + (r - l) //2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid -1
        return l
            
