class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for i in range(len(nums)-1,1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                mx = max(mx , nums[i-2] + nums[i-1] + nums[i] )
        return mx



        