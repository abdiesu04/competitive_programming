class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def calc(mid):
            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True

            return False

        position.sort()
        left, right = 1, position[-1] - position[0]

        while left <= right:
            mid = left + (right - left) // 2
            if calc(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right

