
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        nums = list(cnt.values())
        return gcd(*nums) > 1