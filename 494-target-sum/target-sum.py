class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(sm: int, idx: int) -> int:
            if (sm, idx) in memo:
                return memo[(sm, idx)]
            
            if idx == len(nums):
                return 1 if sm == target else 0
            
            add = backtrack(sm + nums[idx], idx + 1)
            subtract = backtrack(sm - nums[idx], idx + 1)
            
            memo[(sm, idx)] = add + subtract
            return memo[(sm, idx)]

        return backtrack(0, 0)
