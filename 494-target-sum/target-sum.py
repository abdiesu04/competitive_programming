class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backtrack(i, sm):
            if i == len(nums):
                return 1 if sm == target else 0
            
            if (i, sm) in memo:
                return memo[(i, sm)]
            
            memo[(i, sm)] = backtrack(i + 1, sm + nums[i]) + backtrack(i + 1, sm - nums[i])
            
            return memo[(i, sm)]
        
        return backtrack(0, 0)