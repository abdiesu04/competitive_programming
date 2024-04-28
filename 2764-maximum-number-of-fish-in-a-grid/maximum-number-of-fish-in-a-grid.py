class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c, sm):
            visited.add((r, c))
            for rc, cc in directions:
                nr = r + rc
                nc = c + cc
                if inbound(nr, nc) and (nr, nc) not in visited:
                    if grid[nr][nc] != 0:
                        sm[0] += grid[nr][nc]
                        dfs(nr, nc, sm)
            return sm[0]
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    sm = [grid[i][j]]  # Use a list to hold the value of sm
                    ans = max(ans, dfs(i, j, sm))
                   
        return ans