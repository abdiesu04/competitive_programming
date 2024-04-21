# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heappush(heap, diff)
            if len(heap) > ladders:
                bricks = bricks-heapq.heappop(heap)
            if bricks < 0:
                return i
        
        return n-1