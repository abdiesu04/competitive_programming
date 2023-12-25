class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space = 1
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " " and space == 1:
                continue
            elif s[i] != ' ':
                space = 0
                cnt += 1
            elif s[i] == " " and space == 0:
                break
        return cnt
            

        