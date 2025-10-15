class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        cnt = 1

        print(intervals)

        
        for i in range(len(intervals)):

            if intervals[i][0] >= end:
                end = intervals[i][1]
                cnt+=1
            
        return len(intervals) - cnt
        
