from typing import List

class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        intervals: List[Interval] = []

        for emp_intervals in schedule:
            for inter in emp_intervals:
                intervals.append(inter)

        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)

        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev = merged[-1]
            if curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            else:
                merged.append(curr)

        res: List[Interval] = []
        for i in range(1, len(merged)):
            res.append(Interval(merged[i-1].end, merged[i].start))

        return res




        
        