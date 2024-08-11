class Solution:
    def getRow(self, n: int) -> List[int]:
        res = [[1]]

        for i in range(2 ,n+2):
            temp  = []
            calc = [0] + res[i-2] + [0]

            l , r = 0 , 1

            while r < len(calc):
                temp.append(calc[l] + calc[r])
                l += 1
                r += 1
            res.append(temp)

        return res[-1]
