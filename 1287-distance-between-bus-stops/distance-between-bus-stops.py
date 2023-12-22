class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minn = min(start, destination)
        maxx = max(start, destination)
        return min(sum(distance[minn:maxx]), sum(distance[:minn] + distance[maxx:]))        