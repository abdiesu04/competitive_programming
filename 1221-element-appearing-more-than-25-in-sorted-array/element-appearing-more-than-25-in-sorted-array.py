class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mp = {}
        for i in arr:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for key in mp.keys():
            if mp[key] / len(arr) > 0.25:
                return key
            
        