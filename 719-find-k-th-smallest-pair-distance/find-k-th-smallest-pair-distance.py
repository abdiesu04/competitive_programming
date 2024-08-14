class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def counter(mx):
            cnt = 0
            left , right = 0 , 1
            while right < len(nums):
                while nums[right] - nums[left] > mx:
                    left += 1
                cnt += right - left
                right += 1
            return cnt

        left , right  = 0 , nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2
            if counter(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left