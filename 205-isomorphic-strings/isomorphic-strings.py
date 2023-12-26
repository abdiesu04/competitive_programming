class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 , map2 = [], []
        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        
        return map1 == map2
