class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_columns = len(matrix), len(matrix[0])
        l, r = 0, num_rows * num_columns - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // num_columns
            col = mid % num_columns
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False