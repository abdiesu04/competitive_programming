class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total = 0
        count = 0

        for i in range(1 , n +1):
            if i not in banned_set and total + i <= maxSum:
                total += i
                count += 1
        return count
            



