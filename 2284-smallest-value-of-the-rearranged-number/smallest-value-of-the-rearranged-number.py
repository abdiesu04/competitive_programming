class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            num = str(num).strip("-")
            num = sorted(list(num), reverse = True)
            return int("-" + "".join(num))
        zeroes = 0
        nonzero = []
        for i in str(num):
            if int(i):
                nonzero.append(i)
            else:
                zeroes +=1
        nonzero.sort()
        if zeroes:
            # nonzero.sort(reverse = True)
            return int(nonzero[0] + ("0"*zeroes) + "".join(nonzero[1:len(nonzero)]))
        return int("".join(nonzero))