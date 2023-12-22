# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num > 9:
#             nums = list(str(num))
#             num = sum(int(n) for n in nums)
#         return num


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num%9 == 0:
            return 9
        return num%9