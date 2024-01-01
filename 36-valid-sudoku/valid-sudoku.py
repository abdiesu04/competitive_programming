# from collections import defaultdict
# from typing import List

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         col = defaultdict(set)
#         row = defaultdict(set)
#         square = defaultdict(set)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
#                 b = board[r][c]
#                 if b in col[c] or b in row[r] or b in square[(r // 3, c // 3)]:
#                     return False
#                 col[c].add(b)
#                 row[r].add(b)
#                 square[(r // 3, c // 3)].add(b)
#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]

        for i in range(rows):
            for j in range(cols):
                curr = board[i][j]

                if curr == ".":
                    continue
                
                if curr in r[i]:
                    return False
                else:
                    r[i].add(curr)
                
                if curr in c[j]:
                    return False
                else:
                    c[j].add(curr)

                box_num = (i // 3) * 3 + (j // 3)
                if curr in b[box_num]:
                    return False
                else:
                    b[box_num].add(curr)
                
        return True
                
                