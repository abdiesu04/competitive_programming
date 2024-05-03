# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        p1, p2 = 0, 0
        length = min(len(v1), len(v2))
        
        while p1 < length and p2 < length:
            if v1[p1] == v2[p2]:
                p1 += 1
                p2 += 1
            elif v1[p1] > v2[p2]:
                return 1
            elif v1[p1] < v2[p2]:
                return -1
        
        # Compare the remaining parts of v1 and v2
        if len(v1) > length and any(val != 0 for val in v1[length:]):
            return 1
        elif len(v2) > length and any(val != 0 for val in v2[length:]):
            return -1
        
        return 0