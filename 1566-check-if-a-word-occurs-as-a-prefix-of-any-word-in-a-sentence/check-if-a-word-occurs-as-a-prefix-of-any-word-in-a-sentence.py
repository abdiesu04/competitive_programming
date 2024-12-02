class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split() 
        for i, word in enumerate(arr):
            if len(word) >= len(searchWord) and word[:len(searchWord)] == searchWord:
                return i + 1  
        return -1  