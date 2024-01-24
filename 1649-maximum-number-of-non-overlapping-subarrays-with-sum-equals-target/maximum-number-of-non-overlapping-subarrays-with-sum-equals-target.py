class Solution:
    def maxNonOverlapping(self, nums, target):
        num_set = set()
        num_set.add(0)
        count = 0
        total_sum = 0
        for num in nums:
            total_sum += num
            if total_sum - target in num_set:
                count += 1
                num_set = set()
            num_set.add(total_sum)
        return count