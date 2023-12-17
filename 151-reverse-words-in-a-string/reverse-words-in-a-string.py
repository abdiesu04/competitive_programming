class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        return ' '.join(st[::-1])
        