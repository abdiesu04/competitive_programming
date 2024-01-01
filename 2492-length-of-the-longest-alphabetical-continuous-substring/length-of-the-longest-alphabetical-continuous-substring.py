class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        for i in range(len(s) - 1):
            if ord(s[i]) + 1 == ord(s[i+1]):
                l += 1
                ans = max(l, ans)
            else:
                l = 0
        return ans + 1
            
        