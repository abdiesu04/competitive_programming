# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.min_element = list(range(n + 1))
        self.max_element = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        
        if u_root != v_root:
            if self.rank[u_root] < self.rank[v_root]:
                u_root, v_root = v_root, u_root
            
            self.parent[v_root] = u_root
            self.size[u_root] += self.size[v_root]
            self.min_element[u_root] = min(self.min_element[u_root], self.min_element[v_root])
            self.max_element[u_root] = max(self.max_element[u_root], self.max_element[v_root])
            
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] += 1
    
    def get_set_info(self, v):
        root = self.find(v)
        return self.min_element[root], self.max_element[root], self.size[root]


n, m = map(int, input().split())
dsu = DisjointSets(n)

for _ in range(m):
    query, *args = input().split()
    
    if query == "union":
        u, v = map(int, args)
        dsu.union(u, v)
    elif query == "get":
        v = int(args[0])
        min_element, max_element, size = dsu.get_set_info(v)
        print(min_element, max_element, size)