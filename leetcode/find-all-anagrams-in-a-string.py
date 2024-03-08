from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        window = Counter(s[:len(p)])
        res = []

        for i in range(len(s)-len(p)+1):
            if window == pCount:
                res.append(i)
            
            # Update the window by removing the leftmost character and adding the next character
            if i + len(p) < len(s):
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    del window[s[i]]
                window[s[i + len(p)]] += 1

        return res