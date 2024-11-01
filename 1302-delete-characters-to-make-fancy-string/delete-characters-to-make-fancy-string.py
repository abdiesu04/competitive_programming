class Solution:
    def makeFancyString(self, s: str) -> str:
        res  = s[0]
        cnt  = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                # print(cnt , i)
                res += s[i]
        return res

            