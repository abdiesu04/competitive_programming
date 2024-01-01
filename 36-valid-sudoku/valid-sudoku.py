from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                b = board[r][c]
                if b in col[c] or b in row[r] or b in square[(r // 3, c // 3)]:
                    return False
                col[c].add(b)
                row[r].add(b)
                square[(r // 3, c // 3)].add(b)
        return True