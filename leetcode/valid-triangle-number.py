class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        if n < 3:
            return 0
        for i in range(n-1, 1, -1):
            j, k = 0, i - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += k - j
                    k -= 1
                else:
                    j += 1
        return ans