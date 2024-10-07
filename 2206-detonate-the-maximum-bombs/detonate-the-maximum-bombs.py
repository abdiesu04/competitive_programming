class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    distance = sqrt((bombs[j][0] - bombs[i][0])**2 + (bombs[j][1] - bombs[i][1])**2)
                    if distance <= bombs[i][2]:  
                        graph[i].append(j)
                        
       
        def dfs(node, visited):
            visited.add(node)
            count = 1 

            for child in graph[node]:
                if child not in visited:
                    count += dfs(child, visited)

            return count

        ans = 0 

        for i in range(len(bombs)):
            ans = max(ans, dfs(i, set()))  

        return ans
