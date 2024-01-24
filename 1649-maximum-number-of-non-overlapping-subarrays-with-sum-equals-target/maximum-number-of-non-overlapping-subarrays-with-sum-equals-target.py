class Solution:
    def maxNonOverlapping(self, nums, target):
        res = 0
        preSum = set()
        preSum.add(0)
        prev = 0
        for i in range(len(nums)):
            val = prev + nums[i]
            if val - target in preSum:
                res += 1
                preSum = set()
            preSum.add(val)
            prev = val
        return res