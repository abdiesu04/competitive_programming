class Solution:
    def titleToNumber(self, title: str) -> int:
        res = 0
        for i  , s in enumerate(title):
            
            sq = 26 ** (len(title) - i -1)
            res += sq * (ord(s) - ord("A") + 1)
            # print(s ,(len(title) - i-1) , sq , res )
        return res

sol = Solution()
print(sol.titleToNumber("AZY"))