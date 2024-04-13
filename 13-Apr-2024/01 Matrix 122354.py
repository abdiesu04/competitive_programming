# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(r,c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
                    
        while q:
            r , c = q.popleft()
            
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
            
                if inbound(nr,nc) and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] +  1
                    q.append((nr,nc))
                
        return mat