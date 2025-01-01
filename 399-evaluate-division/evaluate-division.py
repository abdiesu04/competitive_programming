class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        def dfs(node, end, val, visited):
            if node == end:
                return val
            visited.add(node)
            
            for child, new_val in graph[node]:
                if child not in visited:
                    res = dfs(child, end, val * new_val, visited)  
                    if res != -1:
                        return res
            return -1
        
        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1)
            else:
                res.append(dfs(start, end, 1, set()))  
        
        return res
