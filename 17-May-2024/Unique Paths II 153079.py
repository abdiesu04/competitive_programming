# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [0] * n
        cur = [0] * n
        prev[n-1] = 1 if grid[m-1][n-1] == 0 else 0  
        
        for i in range(m - 1, -1, -1):
            cur[n-1] = 1 if grid[i][n-1] == 0 and prev[n-1] == 1 else 0  
            
            for j in range(n - 2, -1, -1):
                if grid[i][j] == 1:
                    cur[j] = 0  
                else:
                    cur[j] = cur[j+1] + prev[j] 
            prev = cur[:]  
        return prev[0]