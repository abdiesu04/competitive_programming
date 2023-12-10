#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        isSorted = False
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if order.index(words[i][j]) > order.index(words[i+1][j]):
                        return False
                    isSorted = True
                    break
            if not isSorted:
                if len(words[i]) > len(words[i+1]):
                    return False
# @lc code=end

