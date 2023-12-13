class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=len(s)
        ans=[0]*x
        for i in range(x):
            ans[indices[i]]=s[i]
        return "".join(ans)