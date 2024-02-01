class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        res = []

        # Iterate over the sorted array in steps of 3
        for i in range(0, len(nums), 3):
            # Check if there are at least 3 elements remaining
            if i + 2 < len(nums):
                # If the difference between the maximum and minimum elements in the subarray is greater than k, return an empty list
                if nums[i + 2] - nums[i] > k:
                    return []
                # Append the current subarray to the result
                res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res
                