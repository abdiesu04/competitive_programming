class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        # dp1 tracks the maximum length ending with a positive difference
        # dp2 tracks the maximum length ending with a negative difference
        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # positive difference
                    dp1[i] = max(dp1[i], dp2[j] + 1)
                elif nums[i] < nums[j]:  # negative difference
                    dp2[i] = max(dp2[i], dp1[j] + 1)
        
        return max(dp1[-1], dp2[-1])
