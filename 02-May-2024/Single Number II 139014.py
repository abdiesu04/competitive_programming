# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0 , 32):
            sum = 0
            for n in nums:
                if n < 0:
                    n = n & (2**32-1)
                sum += n >> i & 1
            sum %= 3
            ans |= sum << i
        if ans >= 2**31:
            ans -= 2**32
        return ans