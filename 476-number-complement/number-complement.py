class Solution:
    def findComplement(self, num: int) -> int:
        com = ''
        while num > 0 :
            
            if num % 2 == 1:
                com += '0'
            else:
                com += '1'
            num = num // 2
        return int(com[::-1],2)
        
        