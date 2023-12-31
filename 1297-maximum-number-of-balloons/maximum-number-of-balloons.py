# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         mapp = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
#         for char in text:
#             if char in mapp:
#                 mapp[char] += 1

#         mapp['l'] //= 2
#         mapp['o'] //= 2

#         return min(mapp.values())

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        balloon_count = Counter("balloon")

        res = float('inf')
        s = "balloon"
        for char in s:
            res = min(res, text_count[char] // balloon_count[char])

        return res