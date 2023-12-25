class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        mx = -1
        for i in range(len(nums) -1,-1,-1):
            temp = nums[i]
            nums[i] = mx
            mx = max(nums[i], temp)
        return nums





            

        