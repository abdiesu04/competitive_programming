class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev  = [float('inf')] * n
        prev[src] = 0

        for i in range(k+1):
            cur = prev[:]
            for u , v , w in flights:
                if prev[u] + w < cur[v]:
                    cur[v] = prev[u] + w
            
            prev = cur[:]
        return prev[dst] if prev[dst] != float('inf') else -1