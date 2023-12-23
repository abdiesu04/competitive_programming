class Solution:
    def findMaxConsecutiveOnes(self, n: List[int]) -> int:
        a = 0 
        c= 0 
        for i in n:
            if i != 1 :
                c = max(c , a)
                a= 0 
            else:
                a+= 1 
        return max(c, a) 