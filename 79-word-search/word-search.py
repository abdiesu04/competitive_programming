
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(row, col, word, idx):
            if idx == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[idx]:
                return False
            
            # Mark the current cell as visited
            temp = board[row][col]
            board[row][col] = "#" #anything not letter can be used!
            
            # Explore the neighbors
            found = (backtrack(row + 1, col, word, idx + 1) or
                     backtrack(row - 1, col, word, idx + 1) or
                     backtrack(row, col + 1, word, idx + 1) or
                     backtrack(row, col - 1, word, idx + 1))
            
            # Restore the cell's original value
            board[row][col] = temp
            
            return found
        
        # Iterate through each cell on the board
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, word, 0):
                    return True
        
        return False