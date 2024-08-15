# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])
        
        res = []
        begin, stop = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if stop < start:  
                res.append([begin, stop])
                begin, stop = start, end  
            else: 
                stop = max(stop, end)  
        res.append([begin, stop])

        return res