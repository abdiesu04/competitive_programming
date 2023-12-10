#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        answer = []
        for i in range(len(nums)):
            answer.append(sorted_arr.index(nums[i]))
        return answer




        


         
# @lc code=end

