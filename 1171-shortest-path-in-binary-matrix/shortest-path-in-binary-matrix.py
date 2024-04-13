class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        q = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        while q:
            r, c, length = q.popleft()
            
            if r == n - 1 and c == n - 1:
                return length
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    q.append((nr, nc, length + 1))
                    visited.add((nr, nc))
        
        return -1