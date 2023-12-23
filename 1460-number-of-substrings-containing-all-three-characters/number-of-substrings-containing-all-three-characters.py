class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = j = k = -1
        count = 0
        for index, char in enumerate(s):
            if char == 'a': i = index 
            if char == 'b': j = index 
            if char == 'c': k = index 
            if index > 1:
                count += min(i, j, k) + 1
        return count