# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        safe = [False]*n
        
        while queue:
            # print(queue)
            node = queue.popleft()
            safe[node] = True

            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        res = []
        for i in range(n):
            if safe[i] == True:
                res.append(i)
                
        return res