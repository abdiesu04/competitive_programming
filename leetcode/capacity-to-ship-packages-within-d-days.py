class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            capacity = mid
            count = 1
            for weight in weights:
                if weight > capacity:
                    count += 1
                    if count > days:
                        return True
                    capacity = mid
                capacity -= weight
            return False

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left