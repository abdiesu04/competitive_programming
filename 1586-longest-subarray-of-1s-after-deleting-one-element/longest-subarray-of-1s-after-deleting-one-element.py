class Solution:
        def longestSubarray(self, nums: List[int]) -> int:
            ans = sum = lo = 0
            for hi, num in enumerate(nums):
                sum += num
                while lo < hi and sum < hi - lo:
                    sum -= nums[lo]
                    lo += 1
                ans = max(ans, hi - lo)
            return ans    