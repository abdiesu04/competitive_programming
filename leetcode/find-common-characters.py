class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = words[0]
        res = []
        for i in letters:
            j = 0 
            while j < len(words):
                if i in words[j]:
                    words[j] = words[j].replace(i, '', 1)  # Remove the character from the word
                    j += 1
                else:
                    break
            if j == len(words):
                res.append(i)
        return res