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
                
        