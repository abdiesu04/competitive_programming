class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            if nums[i] != 0 or (nums[i] == 0 and i == len(nums) -1):
                res += cnt *( (cnt+1))//2
                cnt = 0
        return res

        