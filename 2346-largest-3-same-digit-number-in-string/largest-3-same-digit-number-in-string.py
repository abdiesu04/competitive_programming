class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = float('-inf')
        cnt = 1
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                mx = max(mx, int(num[i]))
        return str(mx)*3 if mx != float('-inf') else ""

    


        