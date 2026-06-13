class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        intervals = []

        for emp_intervals in schedule:
            for inter in emp_intervals:
                intervals.append(inter)

        intervals.sort(key = lambda x: x.start)

        merged = [intervals[0]]

        print(intervals)

        for curr in intervals[1:]:

            prev = merged[-1]

            if curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            else:
                merged.append(curr)

        res = []

        for i in range(1, len(merged)):

            res.append(Interval(merged[i-1].end, merged[i].start))

        return res




        
        