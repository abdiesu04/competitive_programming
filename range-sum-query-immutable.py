class NumArray:

    def __init__(self, nums: List[int]):
        self.cum_sum = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.cum_sum[i] = nums[i]
            else:
                self.cum_sum[i] = self.cum_sum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cum_sum[right]
        else:
            return self.cum_sum[right] - self.cum_sum[left-1]
        
    #range-sum