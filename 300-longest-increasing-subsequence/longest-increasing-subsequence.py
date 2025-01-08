class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp , dp[j] + 1)
            dp[i] = temp
        return max(dp)