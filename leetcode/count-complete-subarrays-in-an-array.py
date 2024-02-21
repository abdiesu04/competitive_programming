class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniques = set(nums)
        mapp = defaultdict(int)
        l = 0
        res = 0

        for i in range(len(nums)):
            mapp[nums[i]] += 1
            while len(mapp) == len(uniques):
                res += len(nums) - i
                if mapp[nums[l]] == 1:
                    del mapp[nums[l]]
                else:
                    mapp[nums[l]] -= 1
                l += 1
        return res



        