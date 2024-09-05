# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        

        def backtrack(i ,  comb):
            if len(comb) == k:
                res.append(comb[:])
                return 
            if i > n:
                return 

            comb.append(i)
            backtrack(i + 1 , comb)
            comb.pop()
            backtrack(i + 1 , comb)
        backtrack(1 , [])

        return res
