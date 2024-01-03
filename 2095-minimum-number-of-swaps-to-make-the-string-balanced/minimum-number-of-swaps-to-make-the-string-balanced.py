class Solution:
    def minSwaps(self, s: str) -> int:
        mx = 0 
        cnt = 0
        for i in s:
            if i == '[':
                cnt -= 1
            else:
                cnt += 1
            mx = max(cnt , mx)
        return (mx + 1) //2