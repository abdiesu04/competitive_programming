class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = 0
        while i < len(word):
            if word[i] == ch:
                break
            i += 1
        word = list(word)
        l, r = 0, i
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        return ''.join(word)