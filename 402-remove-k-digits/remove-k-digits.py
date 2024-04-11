class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        
        # Handle the case where k is still greater than 0
        stack = stack[:len(stack)-k]
        
        # Remove leading zeros
        while stack and stack[0] == '0':
            stack.pop(0)
        
        return ''.join(stack) if stack else "0"