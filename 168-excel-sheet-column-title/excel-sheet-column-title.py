class Solution:
    def convertToTitle(self, num: int) -> str:
        res = ""
        while num > 0:
            offset = (num - 1) % 26
            res += chr(ord("A") + offset)
            num = (num -1 ) // 26

        return res[::-1]