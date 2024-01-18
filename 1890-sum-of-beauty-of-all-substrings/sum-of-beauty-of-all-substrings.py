from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i+2,len(s)):
                c=Counter(s[i:j+1])
                v=c.values()
                res+=(max(v)-min(v))
        return res