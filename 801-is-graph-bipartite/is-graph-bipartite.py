
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0 for _ in range(len(graph))]

        def dfs(node , col):
            colors[node] = col
            for child in graph[node]:
                if colors[child] == col:
                    return False
                elif colors[child] == 0:
                    if not dfs(child , 3 - col):
                        return False
            return True
        
        for i in range(len(graph)):
            if colors[i] == 0:
                if not dfs(i , 2):
                    return False
        return True