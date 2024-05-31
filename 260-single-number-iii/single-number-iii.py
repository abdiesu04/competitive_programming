class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mapp = defaultdict(int)
        for i in nums:
            mapp[i] += 1
        res = []
        for key , value in mapp.items():
            if value == 1:
                res.append(key)
        return res

        