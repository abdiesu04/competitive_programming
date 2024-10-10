class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens  , empty , fresh = 0  , 0 , 0
        queue = deque() 

        directions = [(0,1), (0, -1) , (1,0) , (-1,0)]

        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rottens += 1
                    queue.append((row , col))
                else:
                    empty += 1
        time = 0
        while queue:
            if fresh == 0:
                break
            for i in range(len(queue)):
                row , col = queue.popleft()
                for rc , cc in directions:
                    nr , nc  = row + rc , col + cc
                    if inbound(nr , nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                       
                        queue.append((nr , nc))
            time += 1
                        
        return time if fresh == 0 else -1


        