class Solution:
    def longestPalindrome(self, s: str) -> str:
        #for odds
        res = 0
        ans = ''
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s)  and  s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > res:
                ans = s[left+1:right]
                # print(left,right,ans)
                res = right - left - 1  

        #for evens

        for i in range(len(s)-1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > res:
                ans = s[left+1:right]
                # print(left,right,ans)
                res = right - left - 1  

   
        return ans