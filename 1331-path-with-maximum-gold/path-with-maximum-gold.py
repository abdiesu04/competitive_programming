class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def backtrack(row, col, curr_gold):
            nonlocal max_gold

            if 0 <= row < m and 0 <= col < n and grid[row][col] > 0:
                curr_gold += grid[row][col]
                temp = grid[row][col]
                grid[row][col] = 0

                backtrack(row - 1, col, curr_gold)
                backtrack(row + 1, col, curr_gold)
                backtrack(row, col - 1, curr_gold)
                backtrack(row, col + 1, curr_gold)

                grid[row][col] = temp
                max_gold = max(max_gold, curr_gold)

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    backtrack(i, j, 0)

        return max_gold