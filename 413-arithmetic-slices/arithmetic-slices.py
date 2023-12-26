class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        idx = 1
        
        while idx < n:
            diff = nums[idx] - nums[idx - 1]
            count = 1
            while idx < n and nums[idx] - nums[idx - 1] == diff:
                idx += 1
                count += 1
            
            if count >= 3:
                # Add all subarrays
                ans += count * (count + 1) // 2
                
                # Subtract subarrays of length 1 and 2
                ans -= 2 * count - 1
        
        return ans