class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        n = len(grid)
        m = len(grid[0])

        queue = deque([(0,0)])
        time = 1
        visited = set((0,0))

        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m and (row, col) not in visited

        while queue:
            for i in range(len(queue)):
                row , col = queue.popleft()
                if row == n -1 and col == m -1:
                    return time
                for rc , cc in directions:
                    nr , nc  = row + rc , cc + col
                    if inbound(nr, nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        queue.append((nr , nc))
                        visited.add((nr,nc))

            time += 1
        return -1
