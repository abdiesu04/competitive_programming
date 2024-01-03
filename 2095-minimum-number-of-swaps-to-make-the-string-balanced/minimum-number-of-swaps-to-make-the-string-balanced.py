class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for val in s:
            if not stack:
                stack.append(val)
            else:
                if stack[-1] == "[" and val == "]":
                    stack.pop()
                else:
                    stack.append(val)
        b_val = stack.count("[")
        return (b_val + 1) // 2
