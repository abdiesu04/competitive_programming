from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])  # (cell, distance)
        visited = set([1])
        
        while queue:
            curr, distance = queue.popleft()
            
            if curr == n * n:
                return distance
            
            for move in range(1, 7):
                next_cell = curr + move
                
                if next_cell > n * n:
                    break
                
                r, c = self.cellToRC(next_cell, n)
                
                if board[r][c] != -1:
                    next_cell = board[r][c]
                
                if next_cell not in visited:
                    queue.append((next_cell, distance + 1))
                    visited.add(next_cell)
        
        return -1
    
    def cellToRC(self, cell: int, n: int) -> Tuple[int, int]:
        row = (cell - 1) // n
        col = (cell - 1) % n
        
        if row % 2 == 1:
            col = n - 1 - col
        
        row = n - 1 - row
        
        return row, col