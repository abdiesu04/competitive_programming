#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        ans = ''
        for i in command:
            if i == 'G':
                ans += 'G'
            elif i == '(':
                stack.append(i)
            elif i == ')' and stack and stack[-1] == "(":
                stack.pop()
                ans += 'o'
            elif i == ')' and stack and stack[-1] != "(":
                ans += 'al'
                stack.pop()
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return ans

       
# @lc code=end

