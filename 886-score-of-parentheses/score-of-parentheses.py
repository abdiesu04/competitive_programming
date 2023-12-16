class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]   # temp value to help us

        for char in s:
            if char == '(':
                stk.append(0)   # new parent: current sum = 0
            else:
                # An expression will be closed
                # Find its value: either 1 for empty () or 2 * its sub-expressions
                # we can calc both with a simple max()
                value = max(2 * stk.pop(), 1)

                # Add the expression sum to its parent current sum
                #  Assume we have expression E that is (CHD)
                # where C, H, D are valid-subexpressions with values 5, 10, 4
                # then E is (5+10+4) = (19) = 38
                # Every time we finish an expression, we add its value to its parent
                # get the parent and update its sum with a finished sub-expression
                stk[-1] += value

        return stk.pop()
		