class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        lp = points[0][1]
        cnt = 0

        for i in sorted(points):
            if i[0] > lp:
                cnt += 1
                lp = i[1]
            lp = min(lp, i[1])
        return cnt + 1

