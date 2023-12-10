#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = ''
        for i in words:
            if all(i.count(j) <= chars.count(j) for j in i):
                res += i
        return len(res)
        
# @lc code=end

