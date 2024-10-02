class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def findIndex(num):
            left , right = 0 , len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] >= num:
                    right = mid -1
                else:
                    left = mid + 1
            return left

        arr = []
        for i in range(len(nums)):
            if not arr or nums[i] > arr[-1] :
                arr.append(nums[i])
            else:
                idx = findIndex(nums[i])
                arr[idx] = nums[i]

        return len(arr)
