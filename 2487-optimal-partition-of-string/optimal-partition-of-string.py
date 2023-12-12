class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        stack = []
        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                ans += 1
                stack = [i]

        
        return ans + 1