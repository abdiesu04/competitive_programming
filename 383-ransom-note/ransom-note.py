class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = defaultdict(int)
        for char in magazine:
            hash[char] += 1

        for char in ransomNote:
            if hash[char] == 0:
                return False
            hash[char] -= 1
        return True