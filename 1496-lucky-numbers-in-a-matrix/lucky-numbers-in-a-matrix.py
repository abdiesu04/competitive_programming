class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMin , maxCol = [] , []

        for i in range(len(matrix)):
            mn = float('inf')
            for j in range(len(matrix[0])):
                mn = min(mn , matrix[i][j])
            rowMin.append(mn)

        for i in range(len(matrix[0])):
            mx = float('-inf')
            for j in range(len(matrix)):
                mx = max(mx , matrix[j][i])
            maxCol.append(mx)

        lucky = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == maxCol[j]:
                    lucky.append(matrix[i][j])

        return lucky
