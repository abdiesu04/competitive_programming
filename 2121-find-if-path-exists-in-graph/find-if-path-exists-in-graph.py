class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , visited):
            if node == destination:
                return True
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    found = dfs(child ,visited)
                    if found:
                        return True
            return False

        return dfs(source , set())
