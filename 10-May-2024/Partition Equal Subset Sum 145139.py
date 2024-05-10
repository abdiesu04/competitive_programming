# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        dp = {0, nums[0]}
        for i in range(1, len(nums)):
            new_sums = []
            for j in dp:
                new_sum = nums[i] + j
                new_sums.append(new_sum)
                if new_sum == target:
                    return True
            dp.update(new_sums)

        return False