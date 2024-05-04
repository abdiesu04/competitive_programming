# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
  
    def helper(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            ans.append(max(nums[i] + ans[i-2], ans[i-1]))
        
        return ans[-1]