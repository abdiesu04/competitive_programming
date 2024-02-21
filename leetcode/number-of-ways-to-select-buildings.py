class Solution:
    def numberOfWays(self, s: str) -> int:
        count = 0
        n = len(s)
        post_zero = s.count('0')
        prev_zero = 0
        post_ones = s.count('1')
        prev_ones = 0
        
        for i in range(n):
            if s[i] == '0':
                count += prev_ones * post_ones
                post_zero -= 1
                prev_zero += 1
            elif s[i] == '1':
                count += prev_zero * post_zero
                post_ones -= 1
                prev_ones += 1
        
        return count