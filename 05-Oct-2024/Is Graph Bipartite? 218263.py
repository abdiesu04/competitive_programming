# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

        def dfs(node, color):
            colors[node] = color  # Assign the current node a color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:  # If the neighbor hasn't been visited
                    if not dfs(neighbor, 1 - color):  # Assign the opposite color
                        return False
                elif colors[neighbor] == color:  # If the neighbor has the same color
                    return False
            return True

        # We need to check all components in case the graph is disconnected
        for i in range(n):
            if colors[i] == -1:  # If the node hasn't been visited
                if not dfs(i, 0):  # Start DFS with color 0
                    return False

        return True
