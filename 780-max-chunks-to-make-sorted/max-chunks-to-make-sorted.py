
class Solution:
    def maxChunksToSorted(self, nums: List[int]) -> int:
        cnt = 0
        mx = float('-inf') 

        for i in range(len(nums)):
            mx = max(mx, nums[i])  
            if mx == i:
                cnt += 1

        return cnt
