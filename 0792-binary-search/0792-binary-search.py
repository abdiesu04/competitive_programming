class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        right = length  - 1
        left = 0
        

        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
             
            else:
                right = mid - 1
        return -1      

