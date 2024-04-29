class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u , v in edges:
            indegree[v] += 1
        ans = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                ans.append(i)
        # print(ans)
        return ans[0] if len(ans) == 1 else -1

