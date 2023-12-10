#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# # @lc code=start
# class Solution:
    class Solution:
        # def checkPowersOfThree(self, n: int) -> bool:
        #     i = 16
        #     curSum = 0
        #     while i >= 0:
        #         tmp = 3 ** i
        #         if tmp + curSum < n:
        #             curSum += tmp
        #         elif tmp + curSum == n:
        #             return True
        #         i -= 1
        #     return False

        # optimized
        def checkPowersOfThree(self, n: int) -> bool:
            while n > 0:
                if n % 3 == 2:
                    return False
                n //= 3
            return True


               

# @lc code=end

