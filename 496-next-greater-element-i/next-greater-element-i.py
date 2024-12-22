class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(int)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(nextGreater[num] if nextGreater[num] != 0 else -1)
        return res



        