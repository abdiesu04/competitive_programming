class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heappush(heap , -nums[i])
        for i in range(k-1):
            heappop(heap)

        return -heappop(heap)
