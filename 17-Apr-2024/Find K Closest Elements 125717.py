# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, [num, abs(num - x)])
            elif abs(num - x) < heap[0][1]:
                heapq.heapreplace(heap, [num, abs(num - x)])
        res = []
        for _ in range(k):
            num, _ = heapq.heappop(heap)
            res.append(num)
        return res