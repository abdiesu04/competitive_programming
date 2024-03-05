class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def backtrack(i):
            if i == len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            while i < len(nums) - 1 and nums[i] == nums[i  + 1]:
                i += 1
            backtrack(i  + 1)
        backtrack(0)
        return res