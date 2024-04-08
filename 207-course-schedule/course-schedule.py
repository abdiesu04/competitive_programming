from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        completion_status = {}  # Keep track of completion status for each node
        
        def dfs(node):
            if node in visited:
                return completion_status[node]  # Return the completion status of the node
            
            visited.add(node)
            completion_status[node] = False  # Set completion status to False initially
            
            for child in graph[node]:
                if not dfs(child):
                    return False
            
            completion_status[node] = True  # Set completion status to True
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True