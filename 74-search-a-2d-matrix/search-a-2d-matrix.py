class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        low = 0
        high = (r * c) - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid // c][mid % c] < target:
                low = mid + 1
            elif matrix[mid // c][mid % c] > target:
                high = mid - 1
            else:
                return True

        return False