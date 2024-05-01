class Solution:
    def grayCode(self, n: int) -> List[int]:
        v = []
        for i in range(1 << n):
            v.append(i ^ (i >> 1))
        return v