class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapp = defaultdict(int)
        
        for num in arr1:
            mapp[num] += 1

        res = []
        for num in arr2:
            res.extend([num] * mapp[num])
            del mapp[num]  

        remaining = []
        for num, freq in mapp.items():
            remaining.extend([num] * freq)

        res.extend(sorted(remaining))

        return res
