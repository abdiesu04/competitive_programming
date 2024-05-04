# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        memo = [[-1 for _ in range(m)] for _ in range(n)]
        def dfs(r,c):
            if not inbound(r,c):
                return 0
            if r  == n - 1 and c  == m - 1:
                return 1
            if  memo[r][c] == -1:
                memo[r][c] = dfs(r+1,c) + dfs(r,c+1)
            return memo[r][c]
        return dfs(0,0)