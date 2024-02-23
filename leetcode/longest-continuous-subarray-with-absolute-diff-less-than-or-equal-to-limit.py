class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        minqueue = deque()
        maxqueue = deque()

        l = 0
        for r, num in enumerate(nums):
            while minqueue and num > minqueue[-1]:
                minqueue.pop()
            minqueue.append(num)

            while maxqueue and num < maxqueue[-1]:
                maxqueue.pop()
            maxqueue.append(num)

            while minqueue[0] - maxqueue[0] > limit:
                if minqueue[0] == nums[l]:
                    minqueue.popleft()
                if maxqueue[0] == nums[l]:
                    maxqueue.popleft()
                l += 1

            res = max(res, r - l + 1)

            

        return res           