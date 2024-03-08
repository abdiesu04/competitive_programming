class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        posDiag = 0
        negDiag = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i == j:
                    posDiag += mat[i][j]
                elif i + j == len(mat) - 1:
                    negDiag += mat[i][j]
        return posDiag + negDiag