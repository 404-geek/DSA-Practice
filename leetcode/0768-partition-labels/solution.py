class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        ranges = {}

        for i in range(len(s)):

            if s[i] not in ranges:
                ranges[s[i]] = [i]
            
            ranges[s[i]].append(i)

        intervals = list(ranges.values())

        res = [[intervals[0][0], intervals[0][-1]]]

        for inter in range(1, len(intervals)):

            interval = intervals[inter]

            if interval[0] <= res[-1][1]:

                res[-1][1] = max(interval[-1], res[-1][1])

            else:
                res.append([interval[0], interval[-1]])

        return [b-a + 1 for a,b in res]


                
        
