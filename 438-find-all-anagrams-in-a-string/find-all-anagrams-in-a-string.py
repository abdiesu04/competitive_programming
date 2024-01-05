from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pL, sL = len(p), len(s)
        if sL < pL:
            return res
        
        pCount = defaultdict(int)
        sCount = defaultdict(int)

        # Count the frequency of characters in p and the first pL characters in s
        for i in range(pL):
            pCount[p[i]] += 1
            sCount[s[i]] += 1

        # Check if the initial window is an anagram
        if sCount == pCount:
            res.append(0)

        # Slide the window with stride 1
        for i in range(1, sL - pL + 1):
            # Add the rightmost character to the window
            sCount[s[i + pL - 1]] += 1
            # Remove the leftmost character from the window
            sCount[s[i - 1]] -= 1
            if sCount[s[i - 1]] == 0:
                del sCount[s[i - 1]]

            # Check if the current window is an anagram
            if sCount == pCount:
                res.append(i)

        return res