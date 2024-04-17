# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for i , j in cnt.items():
            heappush(heap,(j ,i))
        for i in range(len(heap) - k):
            heappop(heap)
     
        res = []
        for i , j in heap:
            res.append(j)

        return res