class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r-1:
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])