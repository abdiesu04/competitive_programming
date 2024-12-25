class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1,len(target)):
            res += max(0 , target[i] - target[i-1])
        return res