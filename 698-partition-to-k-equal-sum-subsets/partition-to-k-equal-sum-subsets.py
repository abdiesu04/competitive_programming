class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        subset_sums = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            num = nums[index]
            for i in range(k):
                if subset_sums[i] + num <= target_sum:
                    subset_sums[i] += num
                    if backtrack(index + 1):
                        return True
                    subset_sums[i] -= num

                    if subset_sums[i] == 0:
                        break

            return False

        nums.sort(reverse=True) 
        return backtrack(0)