class Solution:
    def countVowels(self, word: str) -> int:
        cnt = 0
        n = len(word)
        for i in range(len(word)):
            if word[i] in "aeiou":
                cnt += (i+ 1) * (n - i)
        return cnt
