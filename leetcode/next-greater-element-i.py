class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []

        for number in nums2:
            while stack and stack[-1] < number:
                nextGreater[stack.pop()] = number
            stack.append(number)

        return [nextGreater.get(i, -1) for i in nums1]
        