class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , w in times:
            graph[u].append((v , w))

        distances = {node:float('inf') for node in range(1 , n+1)}
        distances[k] = 0
        heap = [(0 , k)]
        visited = set()

        while heap:
            dist , node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for child , weight in graph[node]:
                distance  = dist + weight
                if distance < distances[child]:
                    distances[child] = distance
                heappush(heap , (distance , child))

        res = float('-inf')
        for key , val in distances.items():
            res = max(res , val)
        # print(graph)
        # print(distances)
        # print(res)
        return res if res != float(inf) else -1



    