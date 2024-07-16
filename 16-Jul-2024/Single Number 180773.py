# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        for i in range(1,len(nums)):
            temp ^= nums[i]

        return temp
