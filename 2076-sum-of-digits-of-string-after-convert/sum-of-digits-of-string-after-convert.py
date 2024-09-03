class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = self.convert(s)
        for i in range(k):
            s  = self.transform(s)

        return int(s)
        

    def stringToNumber(self , s):
        return ord(s) - ord("a") + 1
        
    def convert(self , s):
        total = ''
        for i in s:
            total += str(self.stringToNumber(i) )
           
        return total

    def transform(self , s):
        result = 0
        for i in s:
            result += int(i)
        return str(result)

