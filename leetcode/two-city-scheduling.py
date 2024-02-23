class Solution:
    def twoCitySchedCost(self, nums: List[List[int]]) -> int:
        res = 0
        diff = []
        for c1 , c2 in nums:
            diff.append([c1-c2, c1 , c2])
        diff.sort()

        for i in range(len(diff)):
            if i < len(diff) / 2:
                res += diff[i][1]
            else:
                res += diff[i][2]
        return res
