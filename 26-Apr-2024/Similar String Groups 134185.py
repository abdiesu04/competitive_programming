# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = [n for n in range(len(strs)+1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            parent[find(u)] = find(v)
        
        def areEq(s1, s2):
            diff = 0
            for ch1, ch2 in zip(s1, s2):
                if ch1 != ch2:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if areEq(strs[i], strs[j]):
                    union(i, j)
        
        cnt = 0
        for i in range(len(strs)):
            if find(i) == i:
                cnt += 1
        
        return cnt