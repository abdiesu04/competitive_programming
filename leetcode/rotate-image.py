class Solution:
    def rotate(self, matrix):
        level = 0
        left = 0
        right = len(matrix[0]) - 1
        n = len(matrix[0]) - 1

        while left < right:
            for i in range(left, right):
                temp = matrix[level][i]
                matrix[level][i] = matrix[n - i][level]
                matrix[n - i][level] = matrix[n - level][n - i]
                matrix[n - level][n - i] = matrix[i][n - level]
                matrix[i][n - level] = temp

            level += 1
            left += 1
            right -= 1


