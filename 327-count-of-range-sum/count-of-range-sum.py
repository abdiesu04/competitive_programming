from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, A, lo, hi):
        S    = [0]
        for x in A:
            S.append( S[-1]  + x )
        #
        P   = SortedList(S)
        #
        res = 0
        for x in S:
            P.remove(x)
            i    = P.bisect_left (lo+x)
            j    = P.bisect_right(hi+x)
            res += max(0,j-i)
        return res