class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        l , r = 0 , len(nums) - k 
        if k == len(nums):
            return nums
        while l < r:
            mid = l + (r - l) // 2
            if x - nums[mid] >  nums[mid+k] - x:
                l = mid + 1
            else:
                r = mid 
        return nums[l:l + k]