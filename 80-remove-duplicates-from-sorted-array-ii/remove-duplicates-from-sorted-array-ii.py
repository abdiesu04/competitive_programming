class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        cnt = 1
        idx = -1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > 2 and idx == -1:
                idx = i
            elif idx != -1 and cnt <= 2:
                nums[idx] = nums[i]
                idx += 1

        return idx if idx != -1 else len(nums)