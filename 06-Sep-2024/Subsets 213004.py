# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []
        def backtrack(index , temp):
            if index == len(nums):
                res.append(temp[:])
                return 
            temp.append(nums[index])
            backtrack(index + 1 , temp)
            temp.pop()
            backtrack(index + 1 , temp)
            

        backtrack(0 , [])
        return res