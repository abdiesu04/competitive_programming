class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_ = max(freq.values())
        res = []

        buckets = [[] for _ in range(max_ + 1)]

        for num , fr in freq.items():
            buckets[fr].append(num)

        for i in range(max_ , 0 , -1):
            res.extend(buckets[i])
            if len(res) >= k:
                break

        return res[:k]

