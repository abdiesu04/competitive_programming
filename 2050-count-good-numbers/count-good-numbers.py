class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2 == 1:
            four = n//2
            five = int(ceil(n/2))
            return ((pow(5, five , 10**9 + 7)) * (pow(4, four, 10**9 + 7)))% (10**9 + 7)
        else:
            four = n//2
            five = n//2
            return ((pow(5, five,10**9 + 7)) * (pow(4, four,10**9 + 7)))% (10**9 + 7)
