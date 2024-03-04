class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(1, [], res, n, k)
        return res
    
    def backtrack(self, i, comb, res, n, k):
        if len(comb) == k:
            res.append(comb[:])
            return
        if i > n:
            return
        comb.append(i)
        self.backtrack(i + 1, comb, res, n, k)
        comb.pop()
        self.backtrack(i + 1, comb, res, n, k)
        print(comb)