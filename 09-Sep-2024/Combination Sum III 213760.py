# Problem: Combination Sum III - https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [1,2,3,4,5,6,7,8,9]
        
        def backtrack(index, comb, total):
            if len(comb) == k:
                if total == n:
                    res.append(comb[:])
                return

            if index >= len(nums) or total >= n:
                return
            
            
            for i in range(index, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb, total + nums[i])
                comb.pop()
        
        backtrack(0, [], 0)
        return res
