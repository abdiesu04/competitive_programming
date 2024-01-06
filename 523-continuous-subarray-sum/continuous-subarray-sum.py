class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     s = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         s += nums[j]
        #         if s % k == 0 :
        #             return True
        # return False

        remainder = {0:-1}
        total = 0

        for i , n in enumerate(nums):
            total += n
            r = total % k

            if r not in remainder:
                remainder[r] = i

            elif i - remainder[r] >= 2:
                return True
        return False