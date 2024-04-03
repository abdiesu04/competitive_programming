class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        per = 0

        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == 0:
                return 1

            if (i, j) in visit:
                return 0

            visit.add((i, j))
            per = 0
            per += dfs(i, j + 1)
            per += dfs(i, j - 1)
            per += dfs(i - 1, j)
            per += dfs(i + 1, j)
            return per

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)