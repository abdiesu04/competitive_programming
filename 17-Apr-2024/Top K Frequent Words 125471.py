# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        heap = []
        for word , cnt in count.items():
            heappush(heap, (-cnt, word))
        
        res = []
        
        for i in range(k):
            res.append(heappop(heap)[1])
        
        return res