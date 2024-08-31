class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index >= len(nums) or nums[i] == 0:
                continue
            
            if nums[index] == 0:
                nums[index] = - abs(nums[i])
            else:
                nums[index] = -abs(nums[index])
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1


