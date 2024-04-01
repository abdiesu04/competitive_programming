class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n-1 , -1 , -1):
            if s[i] == ' ' and cnt == 0:
                continue
            if s[i] == ' ' and cnt > 0:
                break
            else:
                cnt += 1
        return cnt
            