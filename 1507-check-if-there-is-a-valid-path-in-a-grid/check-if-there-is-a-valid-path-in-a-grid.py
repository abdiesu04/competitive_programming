class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        #down=0
        #left=1
        #up=2
        #right=3
        d={
            1:[[],[4,6,1],[],[3,5,1]],
            2:[[2,6,5],[],[2,4,3],[]],
            3:[[5,6,2],[1,4,6],[],[]],
            4:[[6,2,5],[],[],[5,1,3]],
            5:[[],[1,6,4],[2,3,4],[]],
            6:[[],[],[2,3,4],[1,3,5]]
        }

        row=len(grid)
        col=len(grid[0])

        def isvalid(i,j):
            if 0<=i<row and 0<=j<col:
                return True
            return False

        visited=[[False for i in range(col)]for j in range(row)]

        self.op=False

        def dfs(i,j,visited):
            
            if i==row-1 and j==col-1:
                self.op=True
                return
            
            pval=grid[i][j]

            #down
            if isvalid(i+1,j) and visited[i+1][j]==False and grid[i+1][j] in d[pval][0]:
                visited[i+1][j]=True
                dfs(i+1,j,visited)
                visited[i+1][j]=False
            #left
            if isvalid(i,j-1) and visited[i][j-1]==False and grid[i][j-1] in d[pval][1]:
                visited[i][j-1]=True
                dfs(i,j-1,visited)
                visited[i][j-1]=False
            #up
            if isvalid(i-1,j) and visited[i-1][j]==False and grid[i-1][j] in d[pval][2]:
                visited[i-1][j]=True
                dfs(i-1,j,visited)
                visited[i-1][j]=False
            #right
            if isvalid(i,j+1) and visited[i][j+1]==False and grid[i][j+1] in d[pval][3]:
                visited[i][j+1]=True
                dfs(i,j+1,visited)
                visited[i][j+1]=False

        visited[0][0]=True
        dfs(0,0,visited)
        return self.op