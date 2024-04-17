class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for num in piles:
            heappush(heap , -num)
        for i in range(k):
            num = abs(heappop(heap))
            heappush(heap , -ceil(num/2))
        # print(heap)
        return -sum(heap)