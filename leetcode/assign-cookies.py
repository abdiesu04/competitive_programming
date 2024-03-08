class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        total=0
        ind1=ind2=0
        while ind1<len(g) and ind2<len(s):
            if g[ind1]<=s[ind2]:
                total+=1
                ind1+=1
                ind2+=1
            else:ind1+=1
        return total
                