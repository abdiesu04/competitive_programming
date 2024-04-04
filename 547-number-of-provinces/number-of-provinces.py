from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        visited = [False] * n
        count = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count