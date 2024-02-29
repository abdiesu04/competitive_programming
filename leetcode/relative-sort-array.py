class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        leftOvers = [x for x in arr1 if x not in arr2]
        leftOvers.sort()
        arr1.sort()
        result = []
        for i in arr2:
            result.extend([i]*arr1.count(i))
        result.extend(leftOvers)
        return result