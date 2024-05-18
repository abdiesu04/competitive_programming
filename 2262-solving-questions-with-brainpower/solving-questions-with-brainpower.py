class Solution:
    def mostPoints(self, qns: list[list[int]]) -> int:
        @cache
        def go(i: int) -> int:
            if i >= len(qns):
                return 0
            return max(qns[i][0] + go(i + 1 + qns[i][1]), go(i + 1))
           
        
        return go(0)
