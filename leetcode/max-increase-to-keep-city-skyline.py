class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowmax = [max(row) for row in grid]
        colmax = [max(col) for col in zip(*grid)]

        res = 0 

        for i in range(n):
            for j in range(n):
                minmax = min(rowmax[i],colmax[j])
                if grid[i][j] < minmax:
                    res += minmax - grid[i][j]
        return res