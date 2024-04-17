class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for col in row:
                if len(heap) < k:
                    heapq.heappush(heap, -col)
                else:
                    if -col > heap[0]:
                        heapq.heapreplace(heap, -col)
        return -1 * heap[0]