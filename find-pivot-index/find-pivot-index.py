class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = i
            right = i + 1
            if sum(nums[:left]) == sum(nums[right:]):
                return i
                break
        return -1
