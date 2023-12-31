class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapp = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in mapp:
                mapp[char] += 1

        mapp['l'] //= 2
        mapp['o'] //= 2

        return min(mapp.values())