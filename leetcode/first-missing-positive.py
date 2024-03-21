class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (n + 1)
        for i in nums:
            if 0 < i <= n:
                arr[i] = 1
        for i in range(1, n + 1):
            if arr[i] == 0:
                return i
        return n + 1