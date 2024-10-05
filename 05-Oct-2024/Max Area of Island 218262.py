# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1) , (0,-1) , (-1,0) , (1,0)]

        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited  = set()

        def dfs(row , col , visited , area):
            visited.add((row, col))

            for rc , cc in directions:
                nr , nc  = row  + rc , col + cc

                if inbound(nr,nc) and (nr,nc) not in visited and  grid[nr][nc] == 1:
                    area[0] += 1
                    dfs(nr, nc , visited , area)

            return area[0]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area  = [1]
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area  = max(max_area , dfs(i , j, visited , area))
        return max_area


