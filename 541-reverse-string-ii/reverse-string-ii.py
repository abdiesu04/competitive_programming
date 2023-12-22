# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         if k > len(s):
#             return s[::-1]
#         s = list(s)
#         res = []
#         for i in range(0, len(s), 2 * k):
#             res.append(s[i:i+k][::-1])
#             res.append(s[i+k:i+2*k])
#         return ''.join(res)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k > len(s):
            return s[::-1]
        s = list(s)
        res = []
        for i in range(0, len(s), 2 * k):
            res.append(''.join(s[i:i+k][::-1]))
            res.append(''.join(s[i+k:i+2*k]))
        return ''.join(res)