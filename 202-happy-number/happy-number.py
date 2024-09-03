class Solution:
    def isHappy(self, n: int) -> bool:
        visited  = set()
        while True:
            n = self.calc(n)
            if n in visited and n != 1:
                return False
            if n == 1:
                return True
            visited.add(n)

    def calc(self , n):
        res = 0
        s = str(n)
        for i in s:
            res += int(i) * int(i)
        return res