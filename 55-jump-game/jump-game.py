class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        mx = 0 
        for i in range(len(nums) - 1):
            if i > mx:
                return False
            mx = max(mx , nums[i] + i)

        return mx >= len(nums) -1