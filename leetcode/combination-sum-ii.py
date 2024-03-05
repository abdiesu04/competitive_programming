class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() # sort the array to get dupilicates adjacent to eachother
        def backtrack(idx,  path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range (idx ,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue   #keep increment till nums[i] is differnt

                path.append(nums[i])
                backtrack(i+1 , path)
                path.pop()

        backtrack(0 , [])
        return res


        