class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        res = ""
        count = 1
        
        for i in range(1, len(word)):
            if word[i] == word[i - 1] and count < 9:
                count += 1
            else:
                res += str(count) + word[i - 1]
                count = 1
        
        res += str(count) + word[-1]
        
        return res
