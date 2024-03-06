class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        left, right = 0, max(houses[-1], heaters[-1])
        while left < right:
            mid = left + (right - left) // 2
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= mid:
                    i += 1
                else:
                    j += 1
            if i == len(houses):
                right = mid 
            else:
                left = mid + 1
        return left