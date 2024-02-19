class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
       
        for i in range(len(nums)-1):
            if nums[i] > curr:
                curr = nums[i]
            if curr == 0:
                return False
            curr -= 1
        return True