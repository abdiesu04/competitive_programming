class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointer l for s and r for t
        # add l if element is found in t and add r at every iteration
        l , r = 0 , 0 
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1

        return l == len(s)
        