class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        min_queue = deque()
        max_queue = deque()
        left  = 0

        for right  , num in enumerate(nums):
            # remove any number less than num from max_queue

            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)

            # remove any greater number greater than num for min_queue

            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)

            #  shrink the window if the difference is greater than limit

            while  max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1

            res = max(res , right - left + 1)

        return res

            
