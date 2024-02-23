class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                i2 , temp2 = stack.pop()
                res[i2] = i - i2

            stack.append((i, temp))
        return res

                