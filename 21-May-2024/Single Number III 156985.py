# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1=0
        n2=0
        for i in nums :
            n1^=i
        for i in nums:
            if ((n1&(-n1))&i)==0 :
                n2^=i
        return [n1^n2,n2];