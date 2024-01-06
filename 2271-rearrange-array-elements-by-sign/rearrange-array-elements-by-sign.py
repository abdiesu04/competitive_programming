class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        j =1
        n =len(nums)
        ret =[0]*n
        for x in nums:
            if x>0:
                ret[i]=x
                i+=2 
            else:
                ret[j]=x
                j+=2
        return ret
        
        