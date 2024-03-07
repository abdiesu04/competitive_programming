class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for index, interval in enumerate(intervals):
            interval.append(index)
        intervals.sort()

        res = [-1] * len(intervals)

        for _ , end , original_index in intervals:
            index = bisect_left(intervals , [end])
            if index < len(intervals):
                res[original_index] = intervals[index][2]
        return res