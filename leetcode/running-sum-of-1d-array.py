class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total  = 0
        sums = []
        for i in range(len(nums)):
            total += nums[i]
            sums.append(total)
        return sums