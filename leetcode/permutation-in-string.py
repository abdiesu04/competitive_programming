from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_size = len(s1)
        window_count = Counter(s2[:window_size])

        if s1_count == window_count:
            return True

        for i in range(window_size, len(s2)):
            window_count[s2[i - window_size]] -= 1
            if window_count[s2[i - window_size]] == 0:
                del window_count[s2[i - window_size]]
            window_count[s2[i]] += 1

            if s1_count == window_count:
                return True

        return False