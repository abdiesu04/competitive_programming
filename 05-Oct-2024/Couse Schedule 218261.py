# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        #building a graph

        graph = defaultdict(list)

        for u , v in pre:
            graph[v].append(u)

        # create two set one to store if the path has been visited and the other set tp track the visited node

        visited = [False] * numCourses 

        path_visited = [False] * numCourses 

        #define a dfs function 

        def dfs(node):
            #base case
            if path_visited[node]:
                return False
            if visited[node]:
                return True

            visited[node] = True

            path_visited[node] = True

            for child in graph[node]:
                if not dfs(child):
                    return False
                
            path_visited[node] = False
            return True
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True
        