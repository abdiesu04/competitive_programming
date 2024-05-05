class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        hash  = defaultdict(int)
        for i in range(0,len(word)-k+1,k):
            hash[word[i:i+k]] += 1
            i += k
        print(hash)
        return (len(word) -  max(hash.values()) * k)//k