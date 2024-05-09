# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n, memo) :
        if n in memo:
            return memo[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo) + self.helper(n - 3, memo)
            
            return memo[n]