# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         col = defaultdict(set)
#         row = defaultdict(set)
#         n = len(matrix)

#         for r in range(n):
#             for c in range(n):
#                 m = matrix[r][c]
#                 col[c].add(m)
#                 row[r].add(m)

#         for i in col.values():
#             if len(i) < n:
#                 return False

#         for i in row.values():
#             if len(i) < n:
#                 return False
#         return True

        
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = {i for i in range(1, len(matrix) + 1)}
        for row in matrix:
            if set(row) != check:
                return False
        for column in zip(*matrix):
            if set(column) != check:
                return False
        return True