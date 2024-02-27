class Solution:
    def helper(self,nums,p1,p2):
        if not nums:
            if p1 >= p2:
                return True
            return False
        left1,right1,left2,right2 = 0,0,0,0
        if len(nums) >= 2:
            left1 = nums[0]
            left2 = nums[1]
            right1 = nums[-1]
            right2 = nums[-2]
        return (self.helper(nums[2:],p1 + nums[0],p2 + left2) and self.helper(nums[1:len(nums)-1],p1 + nums[0],p2 + right1)) or (self.helper(nums[:-2],p1 + nums[-1],p2 + right2) and self.helper(nums[1:len(nums)-1], p1 + nums[-1], p2 + left1))
    def predictTheWinner(self, nums: List[int]) -> bool:

        return self.helper(nums,0,0)