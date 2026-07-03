class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = []
        max_p = 0
        starts = []

        for s, e, p in zip(startTime, endTime, profit):

            jobs.append((s, e, p))

        jobs.sort()

        for s, e, p in jobs:
            starts.append(s)

        n = len(jobs)

        dp = [0] * n

        dp[-1] = jobs[-1][-1]

        for i in range(n - 2, -1, -1):

            job = jobs[i]

            end = job[1]
            profit = job[2]

            idx = bisect_left(starts, end)

            if idx < n:
                profit += dp[idx]

            skip = dp[i + 1]
            dp[i] = max(profit, skip)

        return dp[0]


