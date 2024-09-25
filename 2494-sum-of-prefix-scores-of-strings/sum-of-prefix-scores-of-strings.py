class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes  = defaultdict(int)

        for word in words:
            for s in range(len(word)):
                prefixes[word[:s+1]] += 1

        result = []
        for word in words:
            ans = 0
            for s in range(len(word)):
                ans += prefixes[word[:s+1]]

            result.append(ans)
        return result