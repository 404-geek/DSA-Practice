class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        times = sorted(zip(startTime, endTime, profit))

        n = len(times)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):

            _, end, prof = times[i]

            insert_pos = bisect_left(times, end, lo = i+1, key = lambda x:x[0])

            dp[i] = max(dp[i+1], prof + dp[insert_pos])

        return dp[0]






        
