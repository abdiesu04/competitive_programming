class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        max_freq = max(freq.values())
        res = []

        buckets = [[] for _ in range(max_freq + 1)]

        for word, fr in freq.items():
            buckets[fr].append(word)

        for i in range(max_freq, 0, -1):
            buckets[i].sort()
            res.extend(buckets[i])
            # if len(res) >= k:
            #     break

        return res[:k]