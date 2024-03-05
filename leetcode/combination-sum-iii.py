class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx, comb, target):
            if len(comb) == k and target == 0:
                res.append(comb[:])
                return

            if len(comb) > k or target < 0:
                return

            for i in range(idx, 10 - k + len(comb) + 1):
                comb.append(i)
                backtrack(i + 1, comb, target - i)
                comb.pop()

        backtrack(1, [], n)
        return res