class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = ''

        for i in sorted(map.items(), key= lambda x : x[1]):
            res += i[0] * i[1]
        return res[::-1]