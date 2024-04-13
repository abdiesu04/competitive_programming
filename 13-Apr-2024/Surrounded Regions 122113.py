# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] != 'O':
                return

            grid[row][col] = 'T'  
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                dfs(nr, nc)

       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1) and grid[i][j] == 'O':
                    dfs(i, j)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == 'T':
                    grid[i][j] = 'O'