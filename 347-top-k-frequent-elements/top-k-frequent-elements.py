from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)
        for i in nums:
            mapp[i] += 1
        res = []
        mapp = sorted(mapp.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            res.append(mapp[i][0])
        return res