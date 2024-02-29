class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        l = 0
        add = 0

        for r in range(n):
            add += nums[r]
            while add >= target:
                ans = min(ans, r-l+1)
                add -= nums[l]
                l += 1

        return 0 if ans == float("inf") else ans

        