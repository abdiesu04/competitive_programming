class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx):
            temp = 0
            cnt = 1
            for i in range(len(nums)):
                if temp + nums[i] <= mx:
                    temp += nums[i]
                else:
                    cnt += 1
                    temp = nums[i]
            return cnt

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = l + (r - l) // 2
            if check(mid) <= k:
                r = mid - 1
            else:
                l = mid + 1
        return l