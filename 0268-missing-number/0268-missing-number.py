class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m  = max(nums)
        for i in range(m+2):
            if i not in nums:
                return i
        return nums[-1] +1
        