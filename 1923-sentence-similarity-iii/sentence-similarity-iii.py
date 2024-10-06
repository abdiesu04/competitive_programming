class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure words1 is the longer sentence
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        # Find the common prefix
        i = 0
        while i < len(words2) and words1[i] == words2[i]:
            i += 1
        
        # Find the common suffix
        j = 0
        while j < len(words2) and words1[-(j+1)] == words2[-(j+1)]:
            j += 1
        
        # If the prefix and suffix together cover the shorter sentence, they are similar
        return i + j >= len(words2)
