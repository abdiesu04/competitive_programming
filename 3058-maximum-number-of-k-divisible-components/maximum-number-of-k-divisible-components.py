class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        cnt = 0  
        visited = set()  

        def dfs(node):
            nonlocal cnt
            visited.add(node)
            
            sm = values[node]
            
            for child in graph[node]:
                if child not in visited:
                    sm += dfs(child)
            
            if sm % k == 0:
                cnt += 1
                return 0  
            
            return sm  
        dfs(0) 
        return cnt
