class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx,  path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range (idx ,len(nums)):
                path.append(nums[i])
                backtrack(i , path)
                path.pop()

        backtrack(0 , [])
        return res

