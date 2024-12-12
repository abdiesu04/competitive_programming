class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heappush(heap, -gift)
        res = 0
        for _ in range(k):
            num = heappop(heap)
            ans = int((-num) ** 0.5)
            heappush(heap, -ans)
            
        res  = 0
        for num in heap:
            res -= num
        
        return res