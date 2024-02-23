class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev=nums[-1]
        count=0
        for i in range(len(nums)-2,-1,-1):
            temp=ceil(nums[i]/prev)
            count+=temp-1
            prev=nums[i]//temp
        return count