#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        l = n // 2
        for i in range(l):
            res.append(n-i)
            res.append(-(n-i))
        if n % 2 != 0:
            res.append(0)
        return res

        
# @lc code=end

