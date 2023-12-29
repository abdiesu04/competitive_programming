class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        d = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                d += 1
        return d