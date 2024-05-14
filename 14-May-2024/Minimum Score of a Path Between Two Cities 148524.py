# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class dsu:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[x for x in range(n+1)]
        self.m=[float("inf") for x in range(n+1)]
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=dsu.find(self,self.parent[x])
        return self.parent[x]
    def f(self):
        return self.m[dsu.find(self,1)]
    def union(self,u,v,w):
        x=dsu.find(self,u)
        y=dsu.find(self,v)
        if x==y:
            self.m[x]=min(self.m[x],w)
            return
        elif self.size[x]>self.size[y]:
            self.size[x]+=self.size[y]
            self.parent[y]=x
            self.m[x]=min(self.m[x],w,self.m[y])
        else:
            self.size[y]+=self.size[x]
            self.parent[x]=y
            self.m[y]=min(self.m[y],w,self.m[x])
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d=dsu(n)
        for i in range(len(roads)):
            d.union(roads[i][0],roads[i][1],roads[i][2])
        return d.f()