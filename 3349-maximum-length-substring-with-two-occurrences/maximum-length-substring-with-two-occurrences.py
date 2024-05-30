class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mapp = defaultdict(int)
        maximum = 0
        counter = 0
        left = 0
        for i in range(len(s)):
            while mapp[s[i]] + 1 > 2:
                maximum = max(maximum, counter)
                counter -= 1
                mapp[s[left]] -= 1
                left += 1
            if mapp[s[i]] + 1 <= 2:
                mapp[s[i]] += 1
                counter += 1
        return max(maximum, counter)