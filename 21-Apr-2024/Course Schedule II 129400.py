# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]
        
        for u , v in pre:
            graph[v].append(u)
        
        order = []
        
        def dfs(course):
            if colors[course] == 1:
                return False
           
            if colors[course] == 2:
                return True
            
            colors[course] = 1
            
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            colors[course] = 2
            order.append(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order[::-1]
            