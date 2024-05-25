class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        return self.backtrack(s, wordDict, memo)

    def backtrack(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return [""]
        
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                for tail in self.backtrack(s[i:], wordDict, memo):
                    print(tail)
                    if tail:
                        res.append(s[:i] + " " + tail)
                    else:
                        res.append(s[:i])
        
        memo[s] = res
        return res