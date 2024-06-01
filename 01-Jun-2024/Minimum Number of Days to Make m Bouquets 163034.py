# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(days):
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets == m:
                    return True
            return bouquets == m

        left, right = 1, max(bloomDay)
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if helper(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans