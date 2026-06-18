from functools import cache
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = []

        for a,b,c in zip(startTime, endTime, profit):

            jobs.append((a,b,c))

        jobs.sort()
        start = []

        for s in jobs:

            start.append(s[0])

        @cache
        def dfs(i):

            if i >= len(jobs):
                return 0

            s, e, pro = jobs[i]

            best_idx = bisect_left(start, e)

            take = pro + dfs(best_idx)
            not_take = dfs(i+1)

            return max(take, not_take)


        return dfs(0)






        