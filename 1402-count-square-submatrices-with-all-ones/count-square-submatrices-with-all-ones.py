class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(1 , len(matrix)):
            for j in range(1 ,len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i][j-1] , matrix[i-1][j] , matrix[i-1][j-1]) + 1
                ans += matrix[i][j]
        
        return ans  + sum(matrix[0]) + sum(row[0] for row in matrix[1:])