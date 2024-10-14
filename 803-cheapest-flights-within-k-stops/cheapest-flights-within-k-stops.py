class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf')]*n
        prev[src] = 0
        for i in range(k+1):
            curr = prev[:]
            for u,v,w in flights:
                if prev[u] + w < curr[v]:
                    curr[v] = prev[u]+w
          
            prev = curr[:]
        return curr[dst] if curr[dst] != float('inf') else -1