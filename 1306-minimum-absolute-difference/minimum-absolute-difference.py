class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mapp = defaultdict(list)

        for i in range(1 , len(nums)):
            diff = nums[i] - nums[i-1]
            mapp[diff].append([nums[i-1] , nums[i]])
        mn = float('inf')
        for key  , val  in mapp.items():
            mn = min(mn , key)
        return mapp[mn]