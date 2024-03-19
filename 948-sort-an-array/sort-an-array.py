from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half: List[int], right_half: List[int]) -> List[int]:
            l, r = 0, 0
            res = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                    res.append(left_half[l])
                    l += 1
                else:
                    res.append(right_half[r])
                    r += 1
            res += left_half[l:]
            res += right_half[r:]
            return res

        def mergeSort(left: int, right: int, arr: List[int]) -> List[int]:
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        return mergeSort(0, len(nums) - 1, nums)