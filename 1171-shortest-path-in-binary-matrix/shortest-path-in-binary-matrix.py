class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        path_length = 1
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        while q:
            size = len(q)
            
            for _ in range(size):
                r, c = q.popleft()
                
                if r == n - 1 and c == n - 1:
                    return path_length
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            path_length += 1
        
        return -1