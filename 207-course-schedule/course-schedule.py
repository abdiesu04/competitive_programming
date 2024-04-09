from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in pre:
            graph[u].append(v)

        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for child in graph[node]:
                if not dfs(child):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True