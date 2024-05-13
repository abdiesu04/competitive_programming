# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        tot_spd, h = 0, []
        ans = -float('inf')
        
        for i, spd in sorted(zip(efficiency, speed),reverse=True):
            while len(h) > k-1:
                tot_spd -= heappop(h)
            heappush(h, spd)
            tot_spd += spd
            ans = max(ans, tot_spd * i)
            
        return ans % (10**9+7)