
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        l , curSum = 0 , 0

        for i in range(len(nums)):
            curSum += nums[i]
            if(i- l + 1) == (2*k+1):
                res[l+k] = curSum// (2*k+1)
                curSum -= nums[l]
                l += 1
        return res