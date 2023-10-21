class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for i in nums:
            count[i] += 1
        arr = count.copy()
        for i in range(1,len(count)):
            count[i] += count[i-1]
        res = []
        for i in nums:
            res.append(count[i] - arr[i] )
        return res


        