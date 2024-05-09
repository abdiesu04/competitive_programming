import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for i in happiness:
            heapq.heappush(heap, -i)

        res = 0
        for i in range(k):
            top = heapq.heappop(heap)
            if top + i < 0:
                res -= top + i
        return res