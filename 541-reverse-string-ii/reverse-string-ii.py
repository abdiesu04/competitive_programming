# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         res = []
#         for i in range(0, len(s), 2 * k):
#             res.append(''.join(s[i:i+k][::-1]))
#             res.append(''.join(s[i+k:i+2*k]))
#         return ''.join(res)

class Solution:
    def reverseStr(self, s:str, k : int) -> str:
        s = list(s)
        for i in range (0, len(s)-1 , 2 * k):
            s[i:k+i] = s[i:k+i][::-1]
        return ''.join(s)
