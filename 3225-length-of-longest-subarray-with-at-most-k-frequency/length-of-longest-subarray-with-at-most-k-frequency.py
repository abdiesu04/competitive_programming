from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        l, r = 0, 0
        ans = 0
        for i in range(len(nums)):
            if cnt[nums[i]] < k:
                cnt[nums[i]] += 1
                r += 1
                ans = max(ans, r - l)
            else:
                # Move the left pointer until the count is less than k
                while l < r and cnt[nums[i]] >= k:
                    cnt[nums[l]] -= 1
                    l += 1
                cnt[nums[i]] += 1
                r += 1
                ans = max(ans, r - l)
                
        return ans