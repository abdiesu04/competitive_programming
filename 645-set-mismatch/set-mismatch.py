class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing  = (n * (n + 1) // 2) - sum(set(nums))

        mapp = defaultdict(int)
        n = len(nums)
        res = []
        for i in range(n):
            mapp[nums[i] - 1] += 1
        print(mapp)
        duplicate = None
        for num , freq in mapp.items():
            if freq > 1:
                duplicate =num + 1


        return [duplicate , missing]