# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        max_jump = 0
        for i in range(len(nums)):
            print(max_jump)
            if max_jump < i:
                return False
            max_jump = max(max_jump , i + nums[i])

        return True