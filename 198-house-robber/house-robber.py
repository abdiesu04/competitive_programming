class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        dp = [nums[0] , nums[1]]

        for i in range(2 , len(nums)):
            temp = max(dp)
            dp[1] = max(dp[1] , nums[i] + dp[0])
            dp[0] = temp
        return max(dp)


