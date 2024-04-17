# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -num)
            largest = -heappop(self.max_heap)
            heappush(self.min_heap, largest)
        else:
            heappush(self.min_heap, num)
            smallest = heappop(self.min_heap)
            heappush(self.max_heap, -smallest)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2.0
        else:
            return float(self.min_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()