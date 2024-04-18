# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for child in graph[course]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        if len(order) != numCourses:
            return []

        return order