class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heappush(self.heap , num)
        
        
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        # print(self.heap)

        for i in range(len(self.heap) -self. k):
            heappop(self.heap)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)