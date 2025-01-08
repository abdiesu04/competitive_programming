class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [0]* (len(edges))

        for i , u in enumerate(edges):
            score[u] += i
        max_idx = 0
        mx = score[0]
        for i in range(len(score)):
            # print(score[i], mx ,max_idx)
            if score[i] > mx:
                max_idx = i
                mx = score[i]
        return max_idx