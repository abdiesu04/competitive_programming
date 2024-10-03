class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # thinking the problem in reverse way and finding then minimum subarray sum of 
        # length n - k

        length  = len(cardPoints) - k

        min_sum = float('inf')

        left = 0
        current = 0
        for right in range(len(cardPoints)):
            current += cardPoints[right]
            while right - left + 1 > length:
                current -= cardPoints[left]
                left += 1
            if right - left + 1 == length:
                min_sum = min(min_sum  , current)

        return sum(cardPoints) - min_sum