class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapp = defaultdict(int)
        n = len(nums)
        res = []
        for i in range(n):
            mapp[nums[i] - 1] += 1
        print(mapp)

        for num , freq in mapp.items():
            if freq > 1:
                res.append(num + 1)


        return res