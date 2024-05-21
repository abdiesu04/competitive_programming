class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dp(idx, k):
            if idx == len(stones) - 1:
                return True
            for i in range(idx + 1, len(stones)):
                diff = stones[i] - stones[idx]
                if diff < k - 1 or diff > k + 1:
                    continue
                if dp(i, diff):
                    return True
            return False

        return dp(0, 0)