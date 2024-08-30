class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1

        # Step 1: Find the first decreasing element from the end
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            # If no such element is found, the list is in descending order
            # So we reverse it to get the smallest permutation
            nums.reverse()
        else:
            # Step 2: Find the element just larger than nums[idx] to the right
            for j in range(len(nums) - 1, idx, -1):
                if nums[j] > nums[idx]:
                    nums[idx], nums[j] = nums[j], nums[idx]
                    break
            
            # Step 3: Reverse the part after idx to get the next smallest lexicographical order
            nums[idx + 1:] = reversed(nums[idx + 1:])
