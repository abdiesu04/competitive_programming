class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 0
        temp = 0
        for i in range(1,n+1):
            temp += i
            if temp <= n:
                cnt += 1
            else:
                break
        return cnt
            
