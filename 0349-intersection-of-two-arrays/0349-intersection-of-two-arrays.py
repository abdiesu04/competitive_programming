class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list(set([x for x in nums1 if x in nums2]))

        return res