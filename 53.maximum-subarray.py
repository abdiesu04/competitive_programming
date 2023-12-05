#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# # @lc code=start
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # res = []
#         # for i in range(len(nums)):
#         #     for j in range(i+1, len(nums)+1):
#         #         res.append(sum(nums[i:j]))
#         # return max(res)
#         #optimize
#         # res = []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(curSum , maxSum)
        return maxSum

        
        
# @lc code=end

