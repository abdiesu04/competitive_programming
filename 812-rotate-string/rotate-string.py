class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # def kmp(p):
        #     n = len(p)
        #     lps = [0] * n
        #     i , j = 0 , 1

        #     while j < len(p):
        #         if p[i] == p[j]:
        #             lps[j] = i + 1
        #             i += 1
        #             j += 1
        #         elif i == 0:
        #             j += 1
        #         else:
        #             i = lps[i-1]
        #     return lps
        # print(kmp(list(s)))
        # return True
        if len(s) == len(goal):
            goal += goal
            return s in goal
        return False