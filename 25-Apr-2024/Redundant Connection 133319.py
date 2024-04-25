# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            if self.isReachable(u, v, graph, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
    
    def isReachable(self, src, dest, graph, visited):
        if src == dest:
            return True
        visited.add(src)
        for neighbor in graph[src]:
            if neighbor not in visited:
                if self.isReachable(neighbor, dest, graph, visited):
                    return True
        return False