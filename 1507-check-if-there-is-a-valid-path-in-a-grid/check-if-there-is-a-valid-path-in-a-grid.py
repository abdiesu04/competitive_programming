class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n , m = len(grid) , len(grid[0])
        directions = {
            1: [(0, -1, [1, 4, 6]), (0, 1, [1, 3, 5])],   # left-right
            2: [(-1, 0, [2, 3, 4]), (1, 0, [2, 5, 6])],   # top-bottom
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])],   # left-bottom
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],    # right-bottom
            5: [(0, -1, [1, 4, 6]), (-1, 0, [2, 3, 4])],  # left-top
            6: [(0, 1, [1, 3, 5]), (-1, 0, [2, 3, 4])]    # right-top
        }

        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m
        visited  = set()

        def dfs(row , col , visited):
            if row == n - 1 and col == m - 1:
                return True
            visited.add((row, col))

            for rc , cc , valid_neighbors in directions[grid[row][col]]:
                nr , nc  = row + rc , col + cc
                if inbound(nr,nc) and grid[nr][nc] in valid_neighbors and (nr,nc) not in visited:
                    if dfs(nr,nc, visited):
                        return True
            return False

        return dfs(0 , 0 , visited)


        