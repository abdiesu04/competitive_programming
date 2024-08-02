class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = nums.count(1)
        if cnt == 0:
            return 0

        nums = nums + nums  
        mx = sum(nums[:cnt])
        cur = mx

        for i in range(cnt, len(nums)):
            cur += nums[i] - nums[i - cnt]
            mx = max(mx, cur)

        res = cnt - mx
        return res

