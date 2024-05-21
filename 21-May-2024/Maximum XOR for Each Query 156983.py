# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        num=0
        for i in nums:
            num^=i
        mx=(2**maximumBit)-1
        res=[]
        for i in range(len(nums)-1,-1,-1):
            res.append(num^mx)
            num^=nums[i]
        return res 
        