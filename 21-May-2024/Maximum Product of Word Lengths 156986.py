# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)                        
        sett = [set(words[i]) for i in range(n)]    
        mx = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (sett[i] & sett[j]): 
                    mx=max(mx, len(words[i]) * len(words[j]))
        
        return mx   