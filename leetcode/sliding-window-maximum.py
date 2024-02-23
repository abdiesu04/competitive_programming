
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_queue = deque()

        
        def clean_deque(i):
           
            if max_queue and max_queue[0] == i - k:
                max_queue.popleft()

           
            while max_queue and nums[i] > nums[max_queue[-1]]:
                max_queue.pop()

        
        for i in range(len(nums)):
            
            clean_deque(i)

            
            max_queue.append(i)

            if i >= k - 1:
                res.append(nums[max_queue[0]])

        return res