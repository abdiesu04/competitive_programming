class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        k = []
        for i in range(len(nums)):
            if nums[i] == target:
                k.append(i)
                
        return k
            