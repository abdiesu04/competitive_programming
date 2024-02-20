class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        sm = []
        for i in range(1, n):
            sm.append(weights[i] + weights[i-1])
        sm.sort()
        min_ = sum(sm[:k-1])
        max_ = sum(sm[::-1][:k-1])
        return max_ - min_