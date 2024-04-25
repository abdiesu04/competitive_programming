# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(u, v):
            ur = find(u)
            vr = find(v)
            if ur == vr:
                return True
            else:
                parent[ur] = vr
                return False

        for u, v in edges:
            if union(u, v):
                return [u, v]
            else:
                union(u , v)