class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for i in s:
            hash1[i] += 1
        for i in t:
            hash2[i] += 1
        return hash1 == hash2