class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heappush(heap , (nums[i] , i))

        for i in range(k):
            num , idx = heappop(heap)
            heappush(heap , (num * multiplier , idx))
        print(heap)
        res  = [0] * len(nums)

        for i in range(len(nums)):
            num  , idx  = heappop(heap)
            res[idx] = num
        
        return res