#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        column , row  = len(matrix[0]), len(matrix)
        res = []
        right , left = 0 , 0 
        up , down = 0 , 0
        while True:
            for i in range(left, column-right):
                res.append(matrix[up][i])
            up += 1
            if up + down == row:
                break
            for i in range(up, row-down):
                res.append(matrix[i][column-1-right])
            right += 1
            if left + right == column:
                break
            for i in range(column-1-right, left-1, -1):
                res.append(matrix[row-1-down][i])
            down += 1
            if up + down == row:
                break
            for i in range(row-1-down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left + right == column:
                break
        return res
# @lc code=end

