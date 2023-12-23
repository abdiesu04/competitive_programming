class Solution:
    def findWords(self, words):
        alphas = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for word in words:
            for row in alphas:
                if all(char.lower() in row for char in word):
                    res.append(word)
                    break
        return res