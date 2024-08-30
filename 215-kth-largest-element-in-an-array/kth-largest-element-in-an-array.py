class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums) - k):
            heappop(nums)

        return heappop(nums)
