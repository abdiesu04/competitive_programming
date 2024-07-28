class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        cnt = numOnes + numZeros
        if k <= cnt:
            return numOnes if numOnes <= k else k

        return numOnes - (k - cnt)
