class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        cnt = 0
        for i in s:
            if i == '(':
                stack.append('(')
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                cnt += 1
        return cnt + len(stack)
