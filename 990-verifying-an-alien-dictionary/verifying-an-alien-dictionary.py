class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Time: O(len(words) * avg word length)
        # Space: O(len(words))
        
        weights = defaultdict(int)
        num = 0
        for i in order:
            weights[i] = num
            num += 1

        for i in range(len(words) - 1):
            # compare adjacent words, words[i] and words[i + 1]
            for j in range(len(words[i])):
                if j + 1 > len(words[i + 1]):
                    # all letters same so far but second word is shorter
                    return False
                elif weights[words[i][j]] < weights[words[i + 1][j]]:
                    # lexicographically sorted, break out of cur loop early
                    break
                elif weights[words[i][j]] == weights[words[i + 1][j]]:
                    # same letters so far, keep comparing
                    continue
                else:
                    # found 1 case where two words are not sorted
                    return False
        
        # all adjacent words have been compared & nothing returned false
        return True
            
        