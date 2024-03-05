class Solution:
    # def helper(self,s,re,n,k):
    #     if n  == 1:
    #         return s[k-1]
    #     if len(s) == (k%2):
    #         return s[k-1]
    #     x = list(s)
    #     s  += re
    #     re  += x

    #     return self.helper(s,re,n-1,k)

    def kthGrammar(self, n: int, k: int) -> int:
        # return int(self.helper(["0"],["1"],n,k))
        return bin(k - 1).count('1') & 1