class Solution:
    def construct2DArray(self, nums: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        size = len(nums)
        if m * n !=  size:
            return []
        cols = size // m
        for i in range(0 , size , cols):
            res.extend([nums[i:i+cols]])
        return res
