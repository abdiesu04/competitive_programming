class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(cols):
            cnt0, cnt1 = 0, 0
            for i in range(rows):
                if grid[i][j] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1

            if cnt0 > cnt1:  
                for i in range(rows):
                    grid[i][j] = 1 - grid[i][j]

        score = 0
        for i in range(rows):
            num = int("".join(map(str, grid[i])), 2)  
            score += num

        return score