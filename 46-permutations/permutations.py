class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res  = []
        def backtrack(path , remaining):
            if not remaining:
                res.append(path)
                return 

            for i in range(len(remaining)):
                new_path = path + [remaining[i]]  
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(new_path ,new_remaining)

        backtrack([] , nums)
        return res