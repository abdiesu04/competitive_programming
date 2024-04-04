class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node , time):
            
            visited.add(node)
            time_taken = 0
            for child in graph[node]:
                if child not in visited:
                    time_taken += dfs(child , 2)
            
            if not hasApple[node] and time_taken == 0:
                return 0

            return time_taken + time
            
        return dfs(0 , 0)

