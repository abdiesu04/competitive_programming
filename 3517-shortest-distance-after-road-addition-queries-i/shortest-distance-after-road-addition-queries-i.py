class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs():
            q = deque([(0, 0)])
            visited = {0}
            while q:
                dist, cur = q.popleft()
                if cur == n - 1:
                    return dist                
                for vertex in graph[cur]:
                    if vertex not in visited:
                        q.append((dist + 1, vertex))
                        visited.add(vertex)

        graph = defaultdict(list)
        for s, d in pairwise(range(n)):
            print(s,d)
            graph[s].append(d)
        result = []
        for s, d in queries:
            graph[s].append(d)
            result.append(bfs())
        return result