# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         d = {}
#         for i in s:
#             d[i] = d.get(i,0) + 1
#         for  val , key in d.items():
#             if key == 1:
#                 return val
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for val, key in d.items():
            if key == 1:
                return s.index(val)
        return -1
        