class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        row, col = len(grid), len(grid[0])
        q = deque()
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in directions:
                    new_r = r + nr
                    new_c = c + nc
                    if inbound(new_r, new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
            time += 1
            
        return time if fresh == 0 else -1