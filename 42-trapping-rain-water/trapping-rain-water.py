class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        mn = 0
        for i in range(n):
            maxLeft[i] = mn
            mn = max(mn , height[i])
        mx = 0
        for i in range(n-1, -1 , -1):
            maxRight[i] = mx
            mx = max(mx  , height[i])
        res  = 0
        for i in range(n):
            tmp = (min(maxRight[i] , maxLeft[i])) -  height[i] 
            if tmp > 0:
                res += tmp
       
        return res