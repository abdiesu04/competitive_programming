class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        for word in s.split():
            ans = (ans * self.count(word)) % MOD
        return ans
            
    def count(self, word):
        n = len(word)
        ans = 1
        for f in Counter(word).values():
            ans *= math.comb(n, f)
            n -= f
        return ans
        