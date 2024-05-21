class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            backtrack(i + 1)
        backtrack(0)
        return res
