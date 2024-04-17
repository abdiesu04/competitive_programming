class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heappush(heap , -num)
        print(heap)
        
        while len(heap) > 1:
            num1 = heappop(heap)
            num2 = heappop(heap)
            if num1 != num2:
                heappush(heap , abs(num1-num2) * -1)
        # print(heap)
        return -heap[0] if heap else 0
            