class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        replacement = {}
        operations = list(reversed(operations))
        for x, y in operations:
            replacement[x] = replacement.get(y, y)
        for idx, val in enumerate(nums):
            if val in replacement:
                nums[idx] = replacement[val]
        return nums