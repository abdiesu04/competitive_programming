class NumArray(object):

    def __init__(self, nums):
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i+1] = self.sum[i] + nums[i]
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        return self.sum[right+1] - self.sum[left]
        """
        :type left: int
        :type right: int
        :rtype: int
