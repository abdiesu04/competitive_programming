class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def edis (x, y):
            return (sqrt(x**2+y**2))
        for i in range(len(points)):
            points[i].append(edis(points[i][0], points[i][1]))
        points.sort(key= lambda x: x[2])
        result = []
        for i in range(k):
            result.append([points[i][0], points[i][1]])
        return (result)