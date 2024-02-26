# Recurrence Solution
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return n
#         return self.fib(n-1) + self.fib(n-2)
        
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        n_0, n_1 = 0, 1
        for i in range(2, n + 1):
            cur = n_0 + n_1
            n_0, n_1 = n_1, cur
        return cur