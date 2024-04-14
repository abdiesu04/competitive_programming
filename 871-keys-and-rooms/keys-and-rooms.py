class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        
        def dfs(node):
            for nei in rooms[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        dfs(0)
        return all(visited)