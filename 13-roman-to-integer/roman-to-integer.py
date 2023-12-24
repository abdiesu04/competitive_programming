class Solution:
    def romanToInt(self, s: str) -> int:
        # start with ans = 0
        #iterate thourgh the string
        #if the next elmnt is greater subtract from and else add to ans
        # return ans
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0

        for i in range(len(s)-1):
            if map[s[i+1]] > map[s[i]]:
                ans -= map[s[i]]
            else:
                ans += map[s[i]]
        return ans + map[s[-1]]

