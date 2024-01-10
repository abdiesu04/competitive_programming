class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res = [0] *len(nums)
        # for i in range(len(nums)):
        #     res[(i+k)%len(nums)] = nums[i]
        # nums[:] = res
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n  # Ensure k is within the range of list length

        reverse(0, n - 1)  # Reverse the entire list
        reverse(0, k - 1)  # Reverse the first k elements
        reverse(k, n - 1)  # Reverse the remaining elements