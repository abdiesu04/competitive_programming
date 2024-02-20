class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref_sum, ans = 0, 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            ans = max(ans, (pref_sum + i) // (i + 1))
        return ans