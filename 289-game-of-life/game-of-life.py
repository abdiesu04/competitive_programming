class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copied = [row[:] for row in board]  # Create a deep copy of the board
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        for row in range(len(board)):
            for col in range(len(board[0])):
                live_cnt, dead_cnt = 0, 0
                # Top
                if inbound(row, col + 1):
                    if copied[row][col + 1] == 1:  # Check top neighbor
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Down
                if inbound(row, col - 1):
                    if copied[row][col - 1] == 1:  # Check down neighbor
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Left
                if inbound(row - 1, col):
                    if copied[row - 1][col] == 1:  # Check left neighbor
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Right
                if inbound(row + 1, col):
                    if copied[row + 1][col] == 1:  # Check right neighbor
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Left-top diagonal
                if inbound(row - 1, col + 1):
                    if copied[row - 1][col + 1] == 1:  # Check left-top diagonal
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Right-top diagonal
                if inbound(row + 1, col + 1):
                    if copied[row + 1][col + 1] == 1:  # Check right-top diagonal
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Left-bottom diagonal
                if inbound(row - 1, col - 1):
                    if copied[row - 1][col - 1] == 1:  # Check left-bottom diagonal
                        live_cnt += 1
                    else:
                        dead_cnt += 1
                # Right-bottom diagonal
                if inbound(row + 1, col - 1):
                    if copied[row + 1][col - 1] == 1:  # Check right-bottom diagonal
                        live_cnt += 1
                    else:
                        dead_cnt += 1

                # Apply the rules of the Game of Life
                if copied[row][col] == 1:
                    if live_cnt < 2:
                        board[row][col] = 0  # Underpopulation
                    elif live_cnt > 3:
                        board[row][col] = 0  # Overpopulation
                else:
                    if live_cnt == 3:
                        board[row][col] = 1  # Reproduction
