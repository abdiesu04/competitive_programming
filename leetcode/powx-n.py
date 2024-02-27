class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n  == 1:
            return x
        if n == -1:
            return 1 / x
        if n == 0 :
            return 1

        return self.myPow(x * x , n//2) if n % 2 == 0 else x * self.myPow(x * x , (n-1)//2)