class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0, len(nums)-1
        s = 0
        n = nums[l] + nums[r]
        while l < r:
            if (nums[l] + nums[r]) == n:
                s += (nums[l] * nums[r])
                l += 1
                r -= 1
            else:
                return -1
        return s

