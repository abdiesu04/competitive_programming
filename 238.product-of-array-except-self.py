#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1]*(len(nums))
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums)-1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res

nums = [1,2,3,4]
for i in range(len(nums)+1):
    for j in range(i+1, len(nums)+1):
        print(nums[i:j])

# @lc code=end

