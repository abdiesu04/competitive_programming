class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i, j):
            if inbound(i, j):
                if grid[i][j] != '0':
                    if grid[i][j] == '1':
                        grid[i][j] = '2'
                        dfs(i, j + 1)
                        dfs(i, j - 1)
                        dfs(i - 1, j)
                        dfs(i + 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)

        return cnt