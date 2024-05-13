class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        p=0
        q=0
        for i in nums :
            p^=i
        for i in nums:
            if ((p&(-p))&i)==0 :
                q^=i
        return [p^q,q];