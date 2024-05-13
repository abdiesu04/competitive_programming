class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for i, j in edges:
            graph[i] += 1
            graph[j] += 1

        for i , val in graph.items():
            if val == len(edges):
                return i