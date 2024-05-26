# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        left, right = 0, n - 1
        min_val = float('inf')
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Update the minimum value
            min_val = min(min_val, nums[mid])
            
            # If the left half is sorted
            if nums[left] <= nums[mid]:
                min_val = min(min_val, nums[left])
                left = mid + 1
            # If the right half is sorted
            else:
                min_val = min(min_val, nums[right])
                right = mid - 1
        
        return min_val