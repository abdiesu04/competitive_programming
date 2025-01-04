class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [False] * (n)
        for u , v in edges:
            indegree[v] = True
        res = []
        for i in range(len(indegree)):
            if not indegree[i]:
                res.append(i)
        return res
