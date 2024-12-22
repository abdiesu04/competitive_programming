class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        n = len(nums)
        doubled_nums = nums + nums  

        for i in range(len(doubled_nums)):
            while stack and stack[-1][1] < doubled_nums[i]:
                idx, _ = stack.pop()
                next_greater[idx % n] = doubled_nums[i]
            stack.append((i, doubled_nums[i]))

        res = []
        for i in range(n):
            res.append(next_greater[i] if i in next_greater else -1)

        return res
