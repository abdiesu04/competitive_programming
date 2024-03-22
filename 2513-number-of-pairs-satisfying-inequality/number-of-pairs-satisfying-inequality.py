class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge_sort(nums):
            if len(nums) <= 1:
                return 0
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            cnt_left = merge_sort(left)
            cnt_right = merge_sort(right)

            i = j = k = c = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    c += len(right) - j
                    i += 1
                else:
                    j += 1

            i = j = k = 0

            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    nums[k] = right[j]
                    j += 1
                else:
                    nums[k] = left[i]
                    i += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

            return cnt_left + cnt_right + c

        new_array = [i -j for i , j in zip(nums1, nums2)]
        return merge_sort(new_array)