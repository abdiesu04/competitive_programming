class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Aproach:
        for every number start with dp array all one assuming every number has atleast one increasing subsequence
        ending with it
        and update the dp based on the previous subsequence ending with it
        """

        dp = [1] * len(nums)
    
        for i in range(len(nums)):
            for j  in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1 , dp[i])

        return max(dp)