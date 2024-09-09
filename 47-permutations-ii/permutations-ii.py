class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path , remaining):
            if not remaining:
                res.append(path[:])
                return 

            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i-1]:
                    continue
                new_remaining = remaining[:i] + remaining[i+1:]
                new_path  = path + [remaining[i]]
                backtrack(new_path , new_remaining)

        backtrack([] , nums)
        return res