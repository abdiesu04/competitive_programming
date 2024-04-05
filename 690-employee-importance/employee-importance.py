from collections import defaultdict

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for employee in employees:
            graph[employee.id] = (employee.importance, employee.subordinates)

        res = 0
        visited = set()

        def dfs(node):
            nonlocal res
            visited.add(node)
            res += graph[node][0]
            for child in graph[node][1]:
                if child not in visited:
                    dfs(child)

        dfs(id)
        return res