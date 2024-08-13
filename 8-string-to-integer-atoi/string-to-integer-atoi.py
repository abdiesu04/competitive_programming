class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore any leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Determine the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Step 3: Convert the integer
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Step 4: Apply rounding based on the 32-bit signed integer range
        result *= sign
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result