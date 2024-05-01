class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        v = []
        for i in range(1 << n):
            v.append(i ^ (i >> 1))
        startidx  = v.index(start)
        return v[startidx:] + v[:startidx]