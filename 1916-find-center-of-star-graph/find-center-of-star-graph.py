class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        o = edges[0][0]
        return o if o in edges[1] else edges[0][1]