# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        required = defaultdict(set)
        for u,v in pre:
            graph[v].append(u)
    
        visited = set()
        def dfs(i,s):
            visited.add(i)
            required[s].add(i)
            for v in graph[i]:
                if v not in visited:
                    dfs(v,s)
        for i in range(numCourses):
            visited.clear()
            dfs(i,i)
        ans = []
        for u,v in queries:
            ans.append((u in required[v]))
        return ans