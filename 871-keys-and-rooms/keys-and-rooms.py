class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])

        queue = deque([0])
        visited  = set([0])

        while queue:
            node = queue.popleft()
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)

        return len(visited) == len(rooms)

