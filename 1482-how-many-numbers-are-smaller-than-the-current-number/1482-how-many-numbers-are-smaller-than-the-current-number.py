class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        result = []

        for i in nums:
            result.append(sortedNums.index(i))

        return result