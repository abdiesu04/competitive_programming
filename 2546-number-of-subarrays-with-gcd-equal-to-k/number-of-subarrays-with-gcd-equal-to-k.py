class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if gcd(*nums[i:j]) == k:
                    cnt += 1
        return cnt