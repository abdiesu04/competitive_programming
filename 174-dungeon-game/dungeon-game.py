class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        memo = [[-1] * m for _ in range(n)]

        def dp(grid, i, j):
            if i == n - 1 and j == m - 1:
                return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
            if i >= n or j >= m:
                return math.inf
            if memo[i][j] != -1:
                return memo[i][j]
            res = grid[i][j] - min(
                dp(grid, i + 1, j),
                dp(grid, i, j + 1)
            )

            memo[i][j] = 1 if res >= 0 else -res 
            return memo[i][j]

        return dp(dungeon, 0, 0)
        