class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i ,( u , v) in enumerate(equations):
            graph[u].append((v , values[i]))
            graph[v].append((u , 1 / values[i]))

        def dfs(node , result , end , visited):
            if node == end:
                return result
            visited.add(node)

            for child , val in graph[node]:
                if child not in visited:
                    found = dfs(child , result * val , end , visited)
                    if found != -1:
                        return found
            return -1
                

        res = []
        for start , end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                ans = dfs(start , 1 , end , set())
                res.append(ans if ans != -1 else -1.0)
        return res
            