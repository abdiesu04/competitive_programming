class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap1 = []
        heap2 = []

        for i in range(len(profits)):
            heappush(heap1, (capital[i], profits[i]))

        while k:
            while heap1 and heap1[0][0] <= w:
                _, profit = heappop(heap1)
                heappush(heap2, -profit)

            if heap2:
                w -= heappop(heap2)
            
            k -= 1

        return w