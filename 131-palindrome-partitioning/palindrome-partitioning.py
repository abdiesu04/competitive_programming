class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        par = []

        def dfs(i):
            if i >= len(s):
                res.append(par.copy())
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    par.append(s[i:j+1])
                    dfs(j+1)
                    par.pop()

        dfs(0)
        return res