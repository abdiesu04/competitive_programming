class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        parent = [i for i in range(n)]

        def find(x): 
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y): 
            x = find(x)
            y = find(y)
            parent[x] = y

        edgeList.sort(key=lambda x : x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key = lambda x : x[2])

        ans = [False for _ in range(len(queries))]
        i  = 0 
        for u, v , l , idx in queries:
            while i < len(edgeList) and l > edgeList[i][2]:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            if find(u) == find(v):
                ans[idx] = True

        return ans
            