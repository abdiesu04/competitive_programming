class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0, res=None):
            if res is None:
                res = []
            
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1, res)
                backtrack(sub + s[i], i + 1, res)
            
            return res
        
        return backtrack()

