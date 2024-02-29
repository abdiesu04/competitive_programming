class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')  # Initialize res to positive infinity
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == target:
                    return sm  # If sum is equal to target, return it immediately
                if abs(sm - target) < abs(res - target):
                    res = sm  # Update res if the current sum is closer to target
                if sm < target:
                    l += 1
                else:
                    r -= 1
        return res