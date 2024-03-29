class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left, right = 0, 0
        result = 0
        max_num = max(nums)
        
        while right < len(nums):
            if nums[right] == max_num:
                count += 1
            
            while count >= k:
                result += len(nums) - right
            
                if nums[left] == max_num:
                    count -= 1
                left += 1
            
            right += 1
        
        return result