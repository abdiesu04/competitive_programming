class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = [nums[0], nums[1]]

        for i in range(2,len(nums)):
            ans.append(nums[i] + max(ans[:i-1]))
        # print(ans)
        return max(ans)