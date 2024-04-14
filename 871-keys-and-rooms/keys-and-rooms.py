class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i].extend(rooms[i])

        visited = set()

        def dfs(node):
            visited.add(node)
            if len(visited) == len(rooms): 
                return True
            for child in graph[node]:
                if child not in visited:
                    if dfs(child):
                        return True
            return False

        return dfs(0)