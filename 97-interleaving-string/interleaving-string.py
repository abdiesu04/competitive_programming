class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} 
        
        def dp(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if k == len(s3):
                return False
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            if i < len(s1) and s1[i] == s3[k]:
                if dp(i + 1, j, k + 1):
                    memo[(i, j, k)] = True
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dp(i, j + 1, k + 1):
                    memo[(i, j, k)] = True
                    return True
            
            memo[(i, j, k)] = False
            return False
        
        return dp(0, 0, 0)