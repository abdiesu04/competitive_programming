class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.pref = [[0 for i in range(n)] for _ in range(m)]

        for i in range(m):
            self.pref[i][0] = matrix[i][0]
            for j in range(1,n):
                self.pref[i][j] = self.pref[i][j-1] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        ans = 0
        for i in range(row1, row2+1):
            after = self.pref[i][col2]
            before = 0
            if col1 > 0:
                before =self.pref[i][col1-1]
            ans+=after-before
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)