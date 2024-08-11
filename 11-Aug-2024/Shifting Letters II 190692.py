# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        move = [0] * len(s)
        for src, dst, dir_ in shifts:
            sign = 1 if dir_ else -1
            move[src] += sign
            if dst+1 < len(move):
                move[dst+1] -= sign
        
        r = 0
        res = list(s)
        for i in range(len(move)):
            r += move[i]
            o = (ord(s[i]) + r - ord('a')) % 26 + ord('a')
            res[i] = chr(o)
        return ''.join(res)