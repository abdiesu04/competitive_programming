class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = [str(n) for n in range(1, n + 1)]
        ranks[:3] = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        maxHeap = []
        for num in score:
            heappush(maxHeap, -num)

        mapp = {}
        for i in range(len(maxHeap)):
            n = heappop(maxHeap)
            mapp[-n] = i

        res = []
        for i in range(len(score)):
            res.append(ranks[mapp[score[i]]])
        return res