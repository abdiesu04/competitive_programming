class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        answer = []
        for i in range(len(nums)):
            answer.append(sorted_arr.index(nums[i]))
        return answer




        


        