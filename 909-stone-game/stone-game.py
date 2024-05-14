class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {} 
        
        def dp(l, r, alice, bob):
            if l == r:
                return alice > bob

            if (l, r, alice, bob) in memo:
                return memo[(l, r, alice, bob)]
            
            if dp(l + 1, r, alice + piles[l], bob):
                memo[(l, r, alice, bob)] = True
                return True
            if dp(l, r - 1, alice + piles[r], bob):
                memo[(l, r, alice, bob)] = True
                return True
            if dp(l + 1, r, alice, bob + piles[l]):
                memo[(l, r, alice, bob)] = True
                return True
            if dp(l, r - 1, alice, bob + piles[r]):
                memo[(l, r, alice, bob)] = True
                return True
            
            memo[(l, r, alice, bob)] = False
            return False
        
        return dp(0, len(piles) - 1, 0, 0)