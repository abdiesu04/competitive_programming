class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap , num)
        for i in range(len(nums)-k):
            heappop(heap)
        return heap[0]