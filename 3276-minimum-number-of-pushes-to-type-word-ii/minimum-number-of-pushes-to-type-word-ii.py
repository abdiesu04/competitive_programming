class Solution:
    def minimumPushes(self, word: str) -> int:
        res = i = 0
        for n in sorted(Counter(word).values(), reverse=True):
            res += n * (i // 8 + 1)
            i += 1
        return res